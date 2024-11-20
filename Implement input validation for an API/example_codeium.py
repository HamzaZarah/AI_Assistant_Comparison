import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn):
    """Create the users table if it does not exist"""
    sql = """CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            );"""
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def register_user(conn, username, password):
    """Register a new user"""
    sql = """INSERT INTO users(username, password) VALUES (?, ?);"""
    try:
        c = conn.cursor()
        c.execute(sql, (username, password))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def main():
    database = "users.db"
    conn = create_connection(database)
    with conn:
        create_table(conn)
        username = input("Enter username: ")
        password = input("Enter password: ")
        if register_user(conn, username, password):
            print("User registered successfully")
        else:
            print("Registration failed")

if __name__ == "__main__":
    main()