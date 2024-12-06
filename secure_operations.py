import sqlite3
import bcrypt
from getpass import getpass

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
    while True:
        username = input("Enter your username: ").strip()
        password = getpass("Enter your password: ").strip()
        if validate_username(username) and validate_password(password):
            break
        else:
            print("----------------------------")
            print("Invalid username or password")
            print("----------------------------")
            print("username must be at least 3 characters in length and contain a digit and a letter")
            print("password must be at least 8 characters in length and contain a digit and at least one instance each of an uppercase and lowercase letter")
            print("----------------------------")
    
    #hantera lösenordet
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
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
    password = getpass("Enter your password: ").strip()
    
    connection = sqlite3.connect("secure_users.db")
    cursor = connection.cursor()
    
    # Säkra SQL-frågor med parametriserade frågor
    cursor.execute("SELECT password_hash, id FROM users WHERE username = ?;", (username,))
    result = cursor.fetchone()
            
    if result and bcrypt.checkpw(password.encode("utf-8"), result[0]):
        user_info = {"username": username, "user_id": result[1]}
        print("Login successful!")
        return user_info
    else:
        print("Login failed!")
    connection.close()

def validate_username(username: str) -> bool:
    """Validate username based on length and contents (must contain letter and digit)"""
    valid_length = False
    has_letter = False
    has_digit = False
    if len(username) > 3:
        valid_length = True
    # Loop over username characters to check for letters and digits
    for char in username:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True
    # Collect conditions in list and use all to verify that they are all met   
    # Returns True if all items are True or list is empty, otherwise returns false
    return all([valid_length, has_letter, has_digit]) 

def validate_password(password: str) -> bool:
    """Validate username based on length and contents (must contain letter and digit)"""
    valid_length = False
    has_letter = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password) > 8:
        valid_length = True
    # Loop over password characters to check for letters and digits
    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_digit = True
    # Collect conditions in list and use all to verify that they are all met   
    # Returns True if all items are True or list is empty, otherwise returns false
    return all([valid_length, has_letter, has_uppercase, has_lowercase, has_digit]) 

def 