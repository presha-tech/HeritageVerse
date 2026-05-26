from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

@app.route("/monument")
def monument():

    return render_template(
        "monument.html"
    )

@app.route("/translator")
def translator():

    return render_template(
        "translator.html"
    )

@app.route("/photobooth")
def photobooth():

    return render_template(
        "photobooth.html"
    )

@app.route("/map")
def map_page():

    return render_template(
        "map.html"
    )

if __name__=="__main__":

    app.run(
        debug=True
    )