# importing the necessary classes
from cleaner import Transform
from config_class import Config
from extract import Extract
from indexing import Index
from loading import LoadData
from split_data import TableData

# defining a main conditional block to create objects and call the methods from the repective classes.
if __name__ == "__main__":
    extract = Extract()
    transform = Transform()
    indexObj = Index()
    tdObj = TableData()
    pdObj = LoadData()
    configObj = Config()
    # defining a dataframe (raw_data) to store the extracted data from the API
    # defining a dataframe (transformed_data) to store the cleaned data
    # defining a dataframe (indexed_data) to store the indexed data
    # defining a dataframe (agencyModel, employeeModel, payrollModel, employeedetailsModel) to store the data after split.
    raw_data = extract.get_data()
    transformed_data = transform.transform_data(raw_data)
    indexed_data = indexObj.index_data(transformed_data)
    agencyModel, employeeModel, payrollModel, employeedetailsModel = tdObj.split(
        indexed_data
    )
    pdObj.create_employee_table(configObj.get_database(configObj.read_config()))
    pdObj.create_employee_details_table(configObj.get_database(configObj.read_config()))
    pdObj.create_payroll_table(configObj.get_database(configObj.read_config()))
    pdObj.create_agency_table(configObj.get_database(configObj.read_config()))
    pdObj.write_table(
        configObj.get_database(configObj.read_config()),
        agencyModel,
        employeeModel,
        payrollModel,
        employeedetailsModel,
    )
