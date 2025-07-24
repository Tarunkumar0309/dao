from employeeService import EmployeeService

def save_employee_data_to_db(employee_list):
    service = EmployeeService()
    service.insertEmployee(employee_list)
    service.close()