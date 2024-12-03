import sqlite3

# Get sqlite3 connection and cursor
def get_connection():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    cursor = connection.cursor("INSERT INTO users VALUES ('admin', 'password')")
    
    return connection, cursor

# INSECURE: No input validation and direct insertion into SQL query
def get_user_from_database(username,password):
    connection, cursor = get_connection()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    
    return user

# INSECURE: Store credentials in plain text le
def store_credentials_to_file(username,password):
    with open("credentials.txt", "w") as file:
        file.write(f"{username:}{password}\n")
        
