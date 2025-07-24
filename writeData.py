from openpyxl import Workbook
from employee import Employee

def writeData(destination, empoyee_list):
    wb = Workbook()
    sheet = wb.active


    for emp in empoyee_list:
        row = [emp.empid, emp.name, emp.age, emp.dept, emp.salary, emp.remarks]
        sheet.append(row)
    wb.save(destination)

