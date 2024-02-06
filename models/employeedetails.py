# EmployeeDetails class
class EmployeeDetails:
    def _int_(self):
        self.employee_id = None
        self.title_description = None
        self.work_location_borough = None
        self.fiscal_year = None
        self.pay_basis = None
        self.base_salary_USD = None
        self.work_hours = None
        self.gross_salary_USD = None
        self.overtime_hours = None
        self.overtime_commission_USD = None
        self.other_pay_USD = None

    # setter function for work_location_borough
    def set_location(self, location):
        self.work_location_borough = location

    # getter function for work_location_borough
    def get_location(self):
        return self.work_location_borough

    # setter function for fiscal_year
    def set_fiscal_year(self, fiscal_year):
        self.fiscal_year = fiscal_year

    # getter function for fiscal_year

    def get_fiscal_year(self):
        return self.fiscal_year


empdetails = EmployeeDetails()
