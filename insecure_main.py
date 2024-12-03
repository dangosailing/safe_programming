import sqlite3
from insecure_operations import store_credentials_to_file, get_user_from_database

username = input("Enter your username: ")
password = input("Enter your password: ")

store_credentials_to_file(username,password)

user = get_user_from_database(username,password)

if user:
    print("Login succesful!")
else:
    print("Login failed!")