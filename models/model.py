# importing required libraries
import sqlite3

# setting database path
from pathlib import Path

# importing objects of tables
from models.employee import emp
from models.employeedetails import empdetails

PROJECT_ROOT = Path(__file__).parents[1]
DB_PATH = PROJECT_ROOT / "database" / "NYC_payroll_data.db"

# DBController class is the main component of Model component of MVC architecture.
class DBController:
    def __init__(self):
        self.cur = None
        self.con = None

    def __int__(self):
        pass

    # defining a function which accepts a id from the user and uses the data mapper object to fetch details from the database about the employuee_id.
    def find_emp(self, id):
        print("Model : Query Received from Controller")
        self._db_connection()
        emp.set_emp_id(id)
        form_query = emp.get_emp_id()
        self.cur.execute(
            f"SELECT employee.employee_id,employee_name,agency_name,fiscal_year,work_location_borough,title_description,work_hours,gross_salary_USD FROM employee JOIN employee_details ON employee.employee_id = employee_details.employee_id JOIN payroll_reference ON employee.employee_id = payroll_reference.employee_id JOIN agency ON payroll_reference.payroll_number = agency.payroll_number WHERE employee.employee_id ={form_query}"
        )

        print("Model: Query Executed. Sending Results back to Controller")
        return self.cur.fetchall()

    # defining a function which display 200 records from the database.
    def view_emp(self):
        print("Model : Query Received from Controller")
        self._db_connection()
        self.cur.execute(
            "select employee.employee_id,employee.employee_name,fiscal_year,work_location_borough,gross_salary_USD from employee INNER JOIN employee_details ON employee.employee_id=employee_details.employee_id limit 200"
        )
        print("Model: Query Executed. Sending Results back to Controller")
        return self.cur.fetchall()

    # defining a function which accepts a location from the user and uses the data mapper object to fetch details from the database about the location.
    def view_emp_from(self, location):
        print("Model : Query Received from Controller")
        self._db_connection()
        empdetails.set_location(location)
        form_query = empdetails.get_location()

        self.cur.execute(
            'select employee.employee_id,employee_name,fiscal_year from employee join employee_details on employee.employee_id=employee_details.employee_id where work_location_borough="{0}"'.format(
                form_query
            )
        )
        print("Model: Query Executed. Sending Results back to Controller")
        return self.cur.fetchall()

    # defining a function which accepts a year from the user and uses the data mapper object to fetch details from the database about the fiscal_year.
    def top_5_earners(self, fiscal_year):
        print("Model : Query Received from Controller")
        self._db_connection()
        empdetails.set_fiscal_year(fiscal_year)
        form_query = empdetails.get_fiscal_year()

        self.cur.execute(
            "select employee.employee_id, employee_name, gross_salary_USD from employee join employee_details on employee.employee_id = employee_details.employee_id where fiscal_year = {0} order by gross_salary_USD desc limit 5".format(
                form_query
            )
        )
        print("Model: Query Executed.Sending Results back to Controller")
        return self.cur.fetchall()

    # defining a helper function to call establish db connection. This will reduce redundant code and improve code readability
    def _db_connection(self):
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()


dbc = DBController()
