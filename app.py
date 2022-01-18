from flask import Flask, render_template, request, redirect
from models import db, locations, dancers, productions, rehearsals, roles, users, role_conflicts, castings
from os import path
from sqlalchemy.orm import aliased

app = Flask(__name__)

if path.expanduser('~') == '/home/aaron':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/flaskballetcasting'
    db.init_app(app)
else:
    print('not running in local development environment, so using other server name')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskballetcasting'
    db.init_app(app)
    
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/documentation', methods=['GET'])
def documentation():
    return render_template("documentation.html")

@app.route('/locations/create', methods=['POST', 'GET'])
def locationscreate():
    if request.method == 'GET':
        #headings = locations.metadata.tables['table1'].columns.keys()
        return render_template("locations_create.html", headings=headings,)
    if request.method == 'POST':
        room = request.form['room']
        building = request.form['building']
        ballet_data.create_location(room, building)
        return redirect('/locations')

@app.route('/locations', methods=['GET'])
def locations_page():
    if request.method == 'GET':
        columns_to_select = [locations.room, locations.building]
        rows = locations.query.with_entities(*columns_to_select)
        return render_template("table.html", headings=columns_to_select, rows=rows)
    
@app.route('/dancers', methods=['POST', 'GET'])
def dancers_page():
    columns_to_select = [dancers.dancer_id, dancers.dancer_fullname, 
                        dancers.dancer_email, dancers.dancer_phone, 
                        dancers.dancer_email_or_phone]
    rows = dancers.query.with_entities(*columns_to_select)
    return render_template("table.html", headings=columns_to_select, rows=rows)
    
@app.route('/productions', methods=['POST', 'GET'])
def productions_page():
    columns_to_select = [productions.prod_id, productions.description]
    rows = productions.query.with_entities(*columns_to_select)
    return render_template("table.html", headings=columns_to_select, rows=rows)

@app.route('/performances', methods=['POST', 'GET'])
def performances_page():
    columns_to_select = [rehearsals.re_id, productions.description, 
                        rehearsals.perf_dt, rehearsals.start_time,
                        rehearsals.end_time]
    headings = ['performance_id', 'performance_description', 
                        'performance_date', 'performance_start_time',
                        'performance_end_time']
    rows = rehearsals.query\
        .join(productions, rehearsals.prod_id == productions.prod_id)\
        .join(locations, rehearsals.location_id == locations.location_id)\
        .filter(rehearsals.is_performance == 1)\
        .filter(productions.is_active == 1)\
        .with_entities(*columns_to_select)
    return render_template("table.html", headings=headings, rows=rows)

@app.route('/rehearsals', methods=['POST', 'GET'])
def rehearsals_page():
    columns_to_select = [rehearsals.re_id, productions.description, 
                        rehearsals.perf_dt, rehearsals.start_time,
                        rehearsals.end_time]
    rows = rehearsals.query\
        .join(productions, rehearsals.prod_id == productions.prod_id)\
        .join(locations, rehearsals.location_id == locations.location_id)\
        .filter(rehearsals.is_performance == 0)\
        .filter(productions.is_active == 1)\
        .with_entities(*columns_to_select)
    return render_template("table.html", headings=columns_to_select, rows=rows)

@app.route('/roles', methods=['POST', 'GET'])
def roles_page():
    columns_to_select = [roles.role_id, productions.description, roles.description, roles.role_count]
    rows = roles.query\
        .join(productions, productions.prod_id == roles.prod_id)\
        .with_entities(*columns_to_select)
    return render_template("table.html", headings=columns_to_select, rows=rows)

@app.route('/castings', methods=['POST', 'GET'])
def castings_page():
    columns_to_select = [castings.casting_id, roles.description, 
                        productions.description, rehearsals.start_time,
                        rehearsals.end_time,    rehearsals.perf_dt,
                        dancers.dancer_fullname,
                        castings.update_dt, rehearsals.is_performance]
    columns = ['casting_id', 'role', 
                'production', 'start_time',
                'end_time', 'perf_dt',
                'name', 'update_dt', 'is_performance']                        
    rows = castings.query\
        .join(roles, castings.role_id == roles.role_id)\
        .join(rehearsals, castings.re_id == rehearsals.re_id)\
        .join(dancers, castings.dancer_id == dancers.dancer_id)\
        .join(productions, rehearsals.prod_id == productions.prod_id)\
        .filter(productions.is_active == 1)\
        .filter(dancers.is_active == 1)\
        .with_entities(*columns_to_select)
    return render_template("table.html", headings=columns, rows=rows)

@app.route('/role_conflicts', methods=['POST', 'GET'])
def role_conflicts_page():
    roles2 = aliased(roles)            
    columns_to_select = [role_conflicts.conflict_id, productions.description, 
                        
                        roles.description, roles2.description]
    columns = ['rc_id', 'production', 
                'role1', 'role2']    
    rows = role_conflicts.query\
        .join(productions, role_conflicts.prod_id == productions.prod_id)\
        .join(roles, role_conflicts.role_id1 == roles.role_id)\
        .join(roles2, role_conflicts.role_id2 == roles2.role_id)\
        .filter(productions.is_active == 1)\
        .with_entities(*columns_to_select)
    return render_template("table.html", headings=columns, rows=rows)

if __name__ == "__main__":
    app.run()