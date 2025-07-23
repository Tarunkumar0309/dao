import mysql.connector

def createconnection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Password@1",
        database="training"
    )
    return conn

def createCursor(conn):
    cursor = conn.cursor()
    return cursor

if __name__ == '__main__':
    try:
        conn = createconnection()
        cursor = createCursor(conn)

        sql = "insert into employee(empid, name, dept) values (%s, %s, %s)"
        empid = int(input("Enter empid to insert: "))
        name = input("Enter employee name: ")
        dept = input("Enter employee department: ")
        values = (empid, name, dept)

        cursor.execute(sql, values)
        conn.commit()
        print("Data inserted")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Failed to insert data: {}".format(err))