from openpyxl import load_workbook
from employee import Employee

def clean_employee_data(data):
    header = data[0]
    rows = data[1:]
    cleaned_rows = [header]

    employee_list = []

    for row in rows:
        empid, name, age, dept, salary, remarks = row

        if empid is None:
            continue

        if name is None:
            name = "Employee"


        emp = Employee(empid = int(empid), name = name, age = int(age), dept =  dept, salary = float(salary), remarks = remarks)
        employee_list.append(emp)
        cleaned_rows.append(row)

    return cleaned_rows, employee_list
