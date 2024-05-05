from flask import Flask, render_template
app = Flask(__name__)

#This is the 'homepage' route
@app.route("/")
def index():
    return render_template("home.html")

# This route is the 'about' page
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
