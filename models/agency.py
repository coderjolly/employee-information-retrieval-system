# Class Agency
class Agency:
    def __init__(self):
        self.payroll_number = None
        self.agency_name = None

    # setter function for payroll_number
    def set_payroll_number(self, pno):
        self.payroll_number = pno

    # setter funtion for agency_name
    def set_agency_name(self, Aname):
        self.agency_name = Aname

    # getter function for payroll_number
    def get_payroll_number(self):
        return self.payroll_number

    # getter function for agency_name
    def get_agency_name(self):
        return self.agency_name


agency = Agency()
