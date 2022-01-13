from flask import Flask, render_template

app = Flask(__name__)

headings = ["Room", "Building", "location_id"]
rows = [   ["Main Stage", "Auditorium Theatre", "1"],
            ["Studio A", "Joffrey Tower", "2"],
            
]
    

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")
    

@app.route('/documentation', methods=['POST', 'GET'])
def documentation():
    return render_template("documentation.html")

@app.route('/locations', methods=['POST', 'GET'])
def locations():
    return render_template("table.html", headings=headings, rows=rows)
    

if __name__ == "__main__":
    app.run()