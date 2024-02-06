# importing required libraries
from flask import Flask, render_template, request
from models import dbc

# Initialising the flask object
app = Flask(__name__, template_folder = "../views/", static_folder="../static/")

# route to render the index.html
@app.route("/")
def index():
    print("Controller: Routing the Index Page for the Client")
    return render_template("index.html",)


# route to render the view.html
@app.route("/view_index")
def view():
    print("Controller : Sending Query to Model")
    rows = dbc.view_emp()
    print("Controller : Received Query Results from Model")
    print("Controller : Routing the HTML Page with Results for the Client")
    return render_template("view.html", rows = rows)


# route to render the find_employee.html
@app.route("/find_emp")
def find():
    print("Controller: Routing the Find Employee Page for the Client")
    return render_template("find_employee.html")


# route to render the find_emp_success.html
@app.route("/emp_info", methods=["POST", "GET"])
def find_id():
    print("Controller : Sending Query to Model")
    id = request.form["id"]
    rows = dbc.find_emp(id)
    print("Controller : Received Query Results from Model")
    if len(rows) == 0:
        print("Controller : Routing the HTML Page with Results for the Client")
        return render_template("find_emp_failed.html")
    print("Controller : Routing the HTML Page with Results for the Client")
    return render_template("find_emp_success.html", rows = rows)


# route to render the top_earners.html
@app.route("/top_earners")
def top_earners():
    print("Controller: Routing the Top Earners Page for the Client")
    return render_template("top_earners.html")


# route to render the earners_success.html
@app.route("/top_earners_filter", methods=["POST", "GET"])
def top_earners_filter():
    print("Controller : Sending Query to Model")
    year = request.form["year"]
    rows = dbc.top_5_earners(year)
    print("Controller : Received Query Results from Model")
    print("Controller : Routing the HTML Page with Results for the Client")
    return render_template("earners_success.html", rows = rows)


# route to render the borough.html
@app.route("/find_emp_by_borough_index")
def filter():
    print("Controller: Routing the Borough Selection Page for the Client")
    return render_template("borough.html")


# route to render the borough_success.html
@app.route("/borough_filter_borough", methods=["POST", "GET"])
def filter_borough():
    print("Controller : Sending Query to Model")
    borough = request.form["borough"]
    rows = dbc.view_emp_from(borough)
    print("Controller : Received Query Results from Model")
    print("Controller : Routing the HTML Page with Results for the Client")
    return render_template("borough_success.html", rows = rows)
