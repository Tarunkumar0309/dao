import mysql.connector
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password@1",
        database="training"
    )

def createCursor(conn):
    return conn.cursor()

def insert_product(conn, cursor, pid, name, category, quantity, price):
    try:
        sql = "insert into products(pid, name, category, quantity, price) values (%s, %s, %s, %s, %s)"
        values = (pid, name, category, quantity, price)
        cursor.execute(sql, values)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        return False

def get_product(cursor):
    sql = "select * from products"
    data = cursor.execute(sql)
    return data

def search_product(cursor, pid):
    sql = "select * from products where pid=%s"
    data = cursor.execute(sql, (pid,))
    return data

def update_product(conn, cursor, pid, new_price):
    sql = "update products set price=%s where pid=%s"
    cursor.execute(sql, (new_price, pid))
    conn.commit()
    if cursor.rowcount == 0:
        return False
    else:
        return True

def delete_product(conn, cursor, pid):
    sql = "delete from products where pid=%s"
    cursor.execute(sql, (pid,))
    conn.commit()
    if cursor.rowcount == 0:
        return False
    else:
        return True