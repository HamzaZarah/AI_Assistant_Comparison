import sqlite3

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('users.db')  # Connect to SQLite database (or create it if it doesn't exist)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL
                        );''')
    except sqlite3.Error as e:
        print(e)

def register_user(username, password):
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully")
    else:
        print("Error! Cannot create the database connection.")

# Example usage
register_user('example_user', 'example_password')
