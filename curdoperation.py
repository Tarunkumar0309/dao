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

def insert_product():
    try:
        conn = createconnection()
        cursor = createCursor(conn)

        sql = "insert into products(pid, name, category, quantity, price) values (%s, %s, %s, %s, %s)"
        pid = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
        values = (pid, name, category, quantity, price)
        cursor.execute(sql, values)
        conn.commit()
        print("Product Added Successfully..!")
    except mysql.connector.Error as error:
        print("Failed to add product..!", error)

def display_product():
    conn = createconnection()
    cursor = createCursor(conn)

    sql = "select * from products"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if rows:
        print("Product Details:")
        for row in rows:
            print(f"PID: {row[0]}, Name: {row[1]}, Category: {row[2]}, Quantity: {row[3]}, Price: {row[4]}")
    else:
        print("No Product Found")

def update_product():
    conn = createconnection()
    cursor = createCursor(conn)

    pid = int(input("Enter product ID: "))
    sql = "select * from products where pid = %s"
    cursor.execute(sql, (pid,))
    rows = cursor.fetchall()
    if rows:
        new_price = float(input("Enter new product price: "))
        sql = "update products set price = %s where pid = %s"
        cursor.execute(sql, (new_price, pid))
        conn.commit()
        print("Product Updated Successfully..!")
    else:
        print("No Product Found")

def delete_product():
    conn = createconnection()
    cursor = createCursor(conn)

    pid = int(input("Enter product ID: "))
    sql = "delete from products where pid = %s"
    cursor.execute(sql, (pid,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Product Deleted Successfully..!")
    else:
        print("No Product Found")

def select_product():
    conn = createconnection()
    cursor = createCursor(conn)

    pid = input("Enter product name: ")
    sql = "select * from products where name = %s"
    cursor.execute(sql, (pid,))
    rows = cursor.fetchall()
    if rows:
        print("Product Details:")
        for row in rows:
            print((f"PID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}"))
    else:
        print("No Product Found")

def menu():
    conn = createconnection()
    cursor = createCursor(conn)

    while True:
        print("_______Product Menu_______")
        print("1. Insert Product")
        print("2. Display Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            insert_product()
        elif choice == 2:
            display_product()
        elif choice == 3:
            update_product()
        elif choice == 4:
            delete_product()
        elif choice == 5:
            select_product()
        elif choice == 6:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

menu()

cursor.close()
conn.close()