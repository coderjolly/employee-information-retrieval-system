# importing required libraries
import sqlite3
import time

import pandas as pd

# defining a class to split the table into smaller data to reduce redundant records and create relationships between data sets.
class TableData:
    def __init__(self):
        pass

    # The split function accepts a large dataframe into 4 different tables called agency, employee, employee_details and payroll_reference
    def split(self, df):
        agency = df[["payroll_number", "agency_name"]]
        agency = agency.drop_duplicates()

        employee = df[["employee_id", "employee_name"]]
        employee = employee.drop_duplicates()

        payroll_reference = df[["payroll_number", "employee_id"]]
        payroll_reference = payroll_reference.drop_duplicates()
        print(df.head())
        # defining the column names in PEP8 standard
        employee_details = df[
            [
                "employee_id",
                "title_description",
                "work_location_borough",
                "fiscal_year",
                "pay_basis",
                "base_salary_USD",
                "work_hours",
                "gross_salary_USD",
                "overtime_hours",
                "overtime_commission_USD",
                "other_pay_USD",
            ]
        ]
        employee_details = employee_details.drop_duplicates()

        return agency, employee, payroll_reference, employee_details
