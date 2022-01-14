from flask import Flask, render_template, request, redirect
from database import db

app = Flask(__name__)

ballet_data = db.localdb()
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/documentation', methods=['GET'])
def documentation():
    return render_template("documentation.html")

@app.route('/locations/create', methods=['POST', 'GET'])
def locationscreate():
    if request.method == 'GET':
        headings = ['room','building']
        return render_template("locations_create.html", headings=headings,)
    if request.method == 'POST':
        room = request.form['room']
        building = request.form['building']
        ballet_data.create_location(room, building)
        return redirect('/locations')

@app.route('/locations', methods=['GET'])
def locations():
    if request.method == 'GET':
        headings, rows = ballet_data.get_table('locations')
        return render_template("table.html", headings=headings, rows=rows)
    
@app.route('/dancers', methods=['POST', 'GET'])
def dancers():
    headings, rows = ballet_data.get_table('dancers')
    return render_template("table.html", headings=headings, rows=rows)
    
@app.route('/productions', methods=['POST', 'GET'])
def productions():
    headings, rows = ballet_data.get_table('productions')
    return render_template("table.html", headings=headings, rows=rows)

#ROUTES FROM HERE DOWN REQUIRE A MORE SPECIALTY QUERIES, NOT GET TABLE

@app.route('/performances', methods=['POST', 'GET'])
def performances():
    headings, rows = ballet_data.get_performances()
    return render_template("table.html", headings=headings, rows=rows)

@app.route('/rehearsals', methods=['POST', 'GET'])
def rehearsals():
    headings, rows = ballet_data.get_rehearsals()
    return render_template("table.html", headings=headings, rows=rows)

@app.route('/roles', methods=['POST', 'GET'])
def roles():
    headings, rows = ballet_data.get_roles()
    return render_template("table.html", headings=headings, rows=rows)

@app.route('/castings', methods=['POST', 'GET'])
def castings():
    headings, rows = ballet_data.get_castings()
    return render_template("table.html", headings=headings, rows=rows)

@app.route('/role_conflicts', methods=['POST', 'GET'])
def role_conflicts():
    headings, rows = ballet_data.get_role_conflicts()
    return render_template("table.html", headings=headings, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)