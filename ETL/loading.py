# importing required libraries
import sqlite3

import pandas as pd

from config_class import Config

# defining a class to load the data to SQLite database
class LoadData:
    def __init__(self):
        self.configObj = Config()
        self.config_df = self.configObj.read_config()

    # method to create table called employee in sqlite database
    def create_employee_table(self, database):
        try:
            database = self.configObj.get_database(self.config_df)
            # sqlite connection/create if not exists
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = """CREATE TABLE IF NOT EXISTS employee (employee_id INT PRIMARY KEY,employee_name TEXT NOT NULL UNIQUE);"""
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            # a helper/internal function called _commit to commit the changes
            self._commit(
                cursor,
                create_table_query,
                sqliteConnection,
                "SQLite table Employee created",
            )

        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)
            cursor.close()

    # method to create table called employee_details in sqlite database
    def create_employee_details_table(self, database):
        try:
            database = self.configObj.get_database(self.config_df)
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = """CREATE TABLE IF NOT EXISTS employee_details (employee_id INT PRIMARY KEY,title_description TEXT,work_location_borough TEXT,fiscal_year INT,pay_basis TEXT,base_salary_USD REAL,work_hours REAL, gross_salary_USD REAL, overtime_hours REAL,overtime_commission_USD REAL, other_pay_USD REAL);"""
            cursor = sqliteConnection.cursor()
            self._commit(
                cursor,
                create_table_query,
                sqliteConnection,
                "SQLite table EmployeeDetails created",
            )

        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)
            cursor.close()

    # method to create table called payroll_reference in sqlite database
    def create_payroll_table(self, database):
        try:
            database = self.configObj.get_database(self.config_df)
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = """CREATE TABLE IF NOT EXISTS payroll_reference (payroll_number INT,employee_id INT PRIMARY KEY);"""
            cursor = sqliteConnection.cursor()
            self._commit(
                cursor,
                create_table_query,
                sqliteConnection,
                "SQLite table Payroll created",
            )

        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)
            cursor.close()

    # method to create table called agency in sqlite database
    def create_agency_table(self, database):
        try:
            database = self.configObj.get_database(self.config_df)
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = """CREATE TABLE IF NOT EXISTS agency (payroll_number INT PRIMARY KEY,agency_name TEXT NOT NULL UNIQUE);"""
            cursor = sqliteConnection.cursor()
            self._commit(
                cursor,
                create_table_query,
                sqliteConnection,
                "SQLite table Agency created",
            )

        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)

    # an internal function to commit the updates to sqlite. This reduces duplicate codes from the existing function.
    def _commit(self, cursor, create_table_query, sqliteConnection, arg3):
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print(arg3)

    # A function to write the data into the tables in sqlite
    def write_table(
        self, database, agency, employee, payroll_reference, employee_details
    ):
        database = self.configObj.get_database(self.config_df)
        sqliteConnection = sqlite3.connect(database)
        # creating an sqlite cursor using the sqlite connection
        cur = sqliteConnection.cursor()

        # using the to_sql() function to send the pandas dataframe to sqlite table and overwrites the data if there is any data.
        try:
            agency.to_sql(
                "agency", sqliteConnection, if_exists="replace", index=False
            )  # writes the pd.df to SQLIte DB
            pd.read_sql("select * from agency", sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading agency table data", error)

        try:
            employee.to_sql(
                "employee", sqliteConnection, if_exists="replace", index=False
            )  # writes the pd.df to SQLIte DB
            pd.read_sql("select * from employee", sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading employee table data", error)

        try:
            payroll_reference.to_sql(
                "payroll_reference", sqliteConnection, if_exists="replace", index=False
            )  # writes the pd.df to SQLIte DB
            pd.read_sql("select * from payroll_reference", sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading payroll table data", error)

        try:
            employee_details.to_sql(
                "employee_details", sqliteConnection, if_exists="replace", index=False
            )  # writes the pd.df to SQLIte DB
            pd.read_sql("select * from employee_details", sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading employee_details table data", error)
        # finally commit the changes through the sqlite connetion
        sqliteConnection.commit()
