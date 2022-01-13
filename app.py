from flask import Flask, render_template
from database import db

app = Flask(__name__)

ballet_data = db.localdb()
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")
    

@app.route('/documentation', methods=['POST', 'GET'])
def documentation():
    return render_template("documentation.html")

@app.route('/locations', methods=['POST', 'GET'])
def locations():
    headings, rows = ballet_data.get_locations()
    return render_template("table.html", headings=headings, rows=rows)
    

if __name__ == "__main__":
    

    app.run()