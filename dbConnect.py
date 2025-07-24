import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Password@1",
        database="training"
    )
    return conn