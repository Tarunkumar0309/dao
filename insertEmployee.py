from dbCursor import get_cursor

class EmployeeDAO:
    def __init__(self):
        self.conn, self.cursor = get_cursor()

    def insertEmployee(self, employee):
        sql = "INSERT INTO employees (empid, name, age, dept, salary, remarks) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (employee.empid, employee.name, employee.age, employee.dept, employee.salary, employee.remarks)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
