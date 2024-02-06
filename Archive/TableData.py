import pandas as pd
from sodapy import Socrata
import time
import sqlite3

data_staging = configdf.query('operation == "Datapull" & configname == "staginglocation"').value.values.tolist()[0]

df = pd.read_csv(data_staging+'NYC_payroll_data_cleaned_indexed.csv',dtype='unicode',engine='python')

def split(df):
    agency = df[['payroll_number','agency_name']]
    agency = agency.drop_duplicates()
    
    employee = df[['employee_id','employee_name']]
    employee = employee.drop_duplicates()
    
    payroll_reference = df[['payroll_number','employee_id']]
    payroll_reference = payroll_reference.drop_duplicates()
    
    employee_details = df[['employee_id','title_description','work_location_borough','fiscal_year','pay_basis','base_salary_USD','work_hours', 'gross_salary_USD', 'overtime_hours','overtime_commission_USD', 'other_pay_USD']]
    employee_details = employee_details.drop_duplicates()
    
    return agency,employee,payroll_reference,employee_details

agency,employee,payroll_reference,employee_details = split(df)

agency.to_csv(data_staging + 'Tables/agency.csv',index=False)
employee_details.to_csv(data_staging + 'Tables/employee_details.csv',index=False)
employee.to_csv(data_staging + 'Tables/employee.csv',index=False)
payroll_reference.to_csv(data_staging + 'Tables/payroll.csv',index=False)