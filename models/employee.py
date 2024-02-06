# Class Employee
class Employee:
    def __int__(self):
        self.employee_id = None
        self.employee_name = None

    # setter function for employee_id

    def set_emp_id(self, id):
        self.employee_id = id

    # setter function for employee_name

    def set_emp_name(self, name):
        self.employee_name = name

    # getter function for employee_id

    def get_emp_id(self):
        return self.employee_id

    # getter function for employee_name

    def get_emp_name(self):
        return self.employee_name


emp = Employee()
