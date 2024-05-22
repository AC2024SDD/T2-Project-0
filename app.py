#This is the Wordle game!

from flask import Flask, render_template, request
app = Flask(__name__)

from wordle import *
game = Game()
print('Testing...')
game.test()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/wordle", methods=["POST", "GET"])
def wordle():
    global game
    if request.method == 'GET':
        game = Game()
    if request.method == "POST":
        guess = request.form.get('guess').lower()
        game.guess('guess')
    return render_template("wordle.html", guesses = game.guesses)

# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=True)
