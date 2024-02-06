import sqlite3
import pandas as pd

configdf = pd.read_csv("configs.csv",quotechar="'")
database = configdf.query('operation == "Pushdata" & configname == "databaselocation"').value.values.tolist()[0]
data_staging = configdf.query('operation == "Datapull" & configname == "staginglocation"').value.values.tolist()[0]

employee = configdf.query('operation == "Pushdata" & configname == "tableemployee"').value.values.tolist()[0]
employee_details = configdf.query('operation == "Pushdata" & configname == "tableempdetails"').value.values.tolist()[0]
payroll_reference = configdf.query('operation == "Pushdata" & configname == "tablepayroll"').value.values.tolist()[0]
agency = configdf.query('operation == "Pushdata" & configname == "tableagency"').value.values.tolist()[0]

def createEmployeeTable(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS employee (employee_id INT PRIMARY KEY,employee_name TEXT NOT NULL UNIQUE);'''
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print("SQLite table Employee created")
    except sqlite3.Error as error:
        print("Error while creating a sqlite table :", error)
        cursor.close()
        
def createEmployeeDetailsTable(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS employee_details (employee_id INT PRIMARY KEY,title_description TEXT,work_location_borough TEXT,fiscal_year INT,pay_basis TEXT,base_salary_USD REAL,work_hours REAL, gross_salary_USD REAL, overtime_hours REAL,overtime_commission_USD REAL, other_pay_USD REAL);'''
        cursor = sqliteConnection.cursor()
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print("SQLite table EmployeeDetails created")
    except sqlite3.Error as error:
        print("Error while creating a sqlite table :", error)
        cursor.close()
        
def createPayrollTable(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS payroll_reference (payroll_number INT,employee_id INT PRIMARY KEY);'''
        cursor = sqliteConnection.cursor()
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print("SQLite table Payroll created")
    except sqlite3.Error as error:
        print("Error while creating a sqlite table :", error)
        cursor.close()
        
def createAgencyTable(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS agency (payroll_number INT PRIMARY KEY,agency_name TEXT NOT NULL UNIQUE);'''
        cursor = sqliteConnection.cursor()
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print("SQLite table Agency created")
    except sqlite3.Error as error:
        print("Error while creating a sqlite table :", error)
        cursor.close()

def writeTable(database,data_staging,agency,employee,employee_details,payroll_reference):
    sqliteConnection = sqlite3.connect(database)
    cur = sqliteConnection.cursor()
    try:
        agencyPath= data_staging+'Tables/agency.csv'
        df1 = pd.read_csv(agencyPath,dtype='unicode',engine='python')
        df1.to_sql(agency, sqliteConnection, if_exists='replace', index=False)
        pd.read_sql('select * from {0}'.format(agency), sqliteConnection)
    except sqlite3.Error as error:
        print("Error while uploading agency table data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
    
    try:
        employeePath= data_staging+'Tables/employee.csv'
        df2 = pd.read_csv(employeePath,dtype='unicode',engine='python')
        df2.to_sql(employee, sqliteConnection, if_exists='replace', index=False)
        pd.read_sql('select * from {0}'.format(employee), sqliteConnection)
    except sqlite3.Error as error:
        print("Error while uploading employee table data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
    try:
        payrollPath= data_staging+'Tables/payroll.csv'
        df3 = pd.read_csv(payrollPath,dtype='unicode',engine='python')
        df3.to_sql('payroll_reference', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
        pd.read_sql('select * from {0}'.format(payroll_reference), sqliteConnection)
    except sqlite3.Error as error:
        print("Error while uploading payroll table data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
    try:
        empdetailsPath= data_staging+'Tables/employee_details.csv'
        df4 = pd.read_csv(empdetailsPath,dtype='unicode',engine='python')
        df4.to_sql(employee_details, sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
        pd.read_sql('select * from {0}'.format(employee_details), sqliteConnection)
    except sqlite3.Error as error:
        print("Error while uploading employee_details table data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

    sqliteConnection.commit()
    sqliteConnection.close()

createEmployeeTable(database)
createEmployeeDetailsTable(database)
createPayrollTable(database)
createAgencyTable(database)
writeTable(database,data_staging,agency,employee,employee_details,payroll_reference)