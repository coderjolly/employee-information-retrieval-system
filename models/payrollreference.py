# PayrollReference class
class PayrollReference:
    def _int_(self):
        self.payroll_number = None
        self.employee_id = None

    # setter function for employee_id
    def set_emp_id(self, id):
        self.employee_id = id

    # setter function for payroll_number
    def set_payroll_number(self, pno):
        self.payroll_number = pno

    # getter function for employee_id
    def get_emp_id(self):
        return self.employee_id

    # getter function for payroll_number
    def get_payroll_number(self):
        return self.payroll_number


payroll = PayrollReference()
