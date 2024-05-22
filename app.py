from flask import Flask, render_template
app = Flask(__name__)

from wordle import *

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/wordle")
def contact():
    print('Guess')
    return render_template("wordle.html")

# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=True)
