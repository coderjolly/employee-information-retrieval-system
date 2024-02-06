import pandas as pd

configdf = pd.read_csv("configs.csv")
data_staging = configdf.query('operation == "Datapull" & configname == "staginglocation"').value.values.tolist()[0]

df = pd.read_csv(data_staging+'NYC_payroll_data.csv',dtype='unicode',engine='python')

def transformdata(df):
    df["employee_name"] = df["first_name"] +' '+ df["mid_init"]+' '+ df["last_name"]
    
    df.drop(columns=['first_name','last_name','mid_init'],axis=1, inplace=True)
    # Renaming Columns

    df.rename(columns={'leave_status_as_of_july_31': 'work_status','regular_hours': 'work_hours', 'base_salary':'base_salary_USD','regular_gross_paid':'gross_salary_USD','ot_hours':'overtime_hours','total_ot_paid':'overtime_commission_USD','total_other_pay':'other_pay_USD'}
,inplace=True, errors='raise')

    df["work_status"].replace({"CEASED": "TERMINATED","SEASONAL" : "CONTRACTUAL"}, inplace=True)

    # formatting date

    df['agency_start_date'] = df['agency_start_date'].str.split('T').str[0]

    df = df[['fiscal_year','payroll_number', 'agency_name', 'agency_start_date',
    'work_location_borough','employee_name', 'title_description', 'work_status',
    'base_salary_USD', 'pay_basis', 'work_hours', 'gross_salary_USD',
    'overtime_hours', 'overtime_commission_USD', 'other_pay_USD']]

    df = df.drop_duplicates()

    df.dropna(subset = ['employee_name'],inplace=True)
    df.dropna(subset = ['title_description'],inplace=True)

    df['employee_name'].astype('str').str.replace(r".", r"", regex=False)
    df['employee_name'].astype('str').str.replace(r"-", r"", regex=False)

    df.sort_values(['fiscal_year', 'employee_name'], ascending=[True, True], inplace=True)
    df['work_location_borough'] = df.groupby(['agency_name'])['work_location_borough'].bfill()
    df.dropna(subset = ['work_location_borough'],inplace=True)

    df.drop(df.loc[df['employee_name']=='xxx xxx'].index, inplace=True)
    df.drop(df.loc[df['pay_basis']=='Prorated Annual'].index, inplace=True)

    cols = df.select_dtypes(object).columns
    df[cols] = df[cols].apply(lambda x: x.str.strip())

    return df
    
transformdata(df).to_csv(data_staging + 'NYC_payroll_data_cleaned.csv')