from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

expenses = []

#This is the 'homepage' route
@app.route("/")
def index():
    return render_template("home.html")

# This route is the 'about' page

@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        expense = request.form["expense"]
        cost = float(request.form["cost"])
        expenses.append([expense, cost])
    return render_template("add_expense.html")

@app.route("/view_total")
def view_total():
    total_cost = sum(cost[1] for cost in expenses)
    return render_template("view_total.html", total=total_cost)

# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
