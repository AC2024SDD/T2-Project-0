from flask import Flask, render_template
app = Flask(__name__)

#This is the 'homepage' route
@app.route("/")
def index():
    return render_template("home.html")

# This route is the 'about' page
@app.route("/add_expense")
def about():
    return render_template("add_expense.html")

@app.route("/view_total")
def contact():
    return render_template("view_total.html")

# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
