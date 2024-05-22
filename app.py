from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)

#This is the 'homepage' route
@app.route("/")
def index():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template('login.html')


def add_expenses(expense, cost):
    with open('expenses.csv', 'a', newline='', encoding='utf-8') as file:  # Use 'a' for append mode
        writer = csv.writer(file)
        writer.writerow([expense, cost])


def load_expenses_from_csv():
    expenses = []
    with open('expenses.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses

@app.route("/add_expense", methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        expense = request.form['expense']
        cost = request.form['cost']
        add_expenses(expense, cost)
        return redirect(url_for('view_total'))
    return render_template("add_expense.html")

@app.route("/view_total")
def view_total():
    exp = load_expenses_from_csv()
    total_cost = sum(float(row['cost']) for row in exp)  # Calculate the total cost
    return render_template("view_total.html", exp=exp, total_cost=total_cost)

@app.route("/advice")
def advice():
    return render_template("advice.html")

# Here's how you create a route
# @app.route("/routeName")
# def functionName():
#    return render_template("fileName.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
