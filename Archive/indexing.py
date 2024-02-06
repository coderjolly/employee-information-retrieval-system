import pandas as pd

configdf = pd.read_csv("configs.csv")
data_staging = configdf.query('operation == "Datapull" & configname == "staginglocation"').value.values.tolist()[0]

df = pd.read_csv(data_staging+'NYC_payroll_data_cleaned.csv',dtype='unicode',engine='python')

def indexdata(df):

    inputset = set(df['employee_name'].tolist())

    inputset2 = set(df['agency_name'].tolist())

    output_dict = {val+1024:item for val,item in enumerate(inputset)}

    output_dict2 = {val+100:item for val,item in enumerate(inputset2)}

    df_emp = pd.DataFrame(output_dict.items(), columns=['employee_id', 'employee_name'])

    df_agency = pd.DataFrame(output_dict2.items(), columns=['payroll_number', 'agency_name'])

    if df_agency.agency_name.nunique() == df_agency.payroll_number.nunique():
        df.drop(['payroll_number'], axis = 1, inplace = True)
        
    final_df = df.merge(df_emp,on = 'employee_name')
    final_df = final_df.merge(df_agency,on = 'agency_name')
    
    print(final_df.columns)

    final_df.drop(columns=df.columns[0], axis=1, inplace=True)
    first_col = final_df.pop('employee_id')
    final_df.insert(0, 'employee_id',first_col)

    second_col = final_df.pop('payroll_number')
    final_df.insert(1, 'payroll_number',second_col)
    
    return final_df

indexdata(df).to_csv(data_staging + 'NYC_payroll_data_cleaned_indexed.csv',index=False)