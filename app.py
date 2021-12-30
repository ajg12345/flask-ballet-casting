from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")
    

@app.route('/documentation', methods=['POST', 'GET'])
def documentation():
    return render_template("documentation.html")
    

if __name__ == "__main__":
    app.run()