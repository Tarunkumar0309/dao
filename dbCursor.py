from dbConnect import get_connection

def get_cursor():
    conn = get_connection()
    cursor = conn.cursor()
    return conn, cursor