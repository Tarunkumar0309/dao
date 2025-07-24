from insertEmployee import EmployeeDAO

class EmployeeService:
    def __init__(self):
        self.employeeDAO = EmployeeDAO()

    def insertEmployee(self, employee_list):
        for employee in employee_list:
            self.employeeDAO.insertEmployee(employee)

    def close(self):
        self.employeeDAO.close()