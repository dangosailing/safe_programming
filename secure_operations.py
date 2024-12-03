import sqlite3
import bcrypt

# Create a table to store users with hashed passwords
def create_user_table():
    """Create a table to store users with hashed passwords."""
    connection = sqlite3.connect("secure_users.db")
    cursor = connection.cursor()
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY,
           username TEXT NOT NULL UNIQUE,
           password_hash TEXT NOT NULL
       )            
    """    
    )
    connection.commit()
    connection.close()
    
def register_user():
    """Registers a new user with a hashed password"""
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    #hantera lösenordet
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    print(hashed_password)
    connection = sqlite3.connect("secure_users.db")
    cursor = connection.cursor()
    
    try:
        query = "INSERT INTO users (username,password_hash) VALUES (?,?)"
        cursor.execute(query, (username, hashed_password))
        connection.commit()
        print("User registered succesfully")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    finally:
        connection.close()
        
# SECURE: Verify user credentials with hashed password
def login_user():
    """Verify user credentials and login."""
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    connection = sqlite3.connect("secure_users.db")
    cursor = connection.cursor()
    
    # Säkra SQL-frågor med parametriserade frågor
    cursor.execute("SELECT password_hash FROM users WHERE username = ?;", (username,))
    result = cursor.fetchone()
    
    if result and bcrypt.checkpw(password.encode("utf-8"), result[0]):
        print("Login successful!")
        
    else:
        print("Login failed!")
    connection.close()
