from secure_operations import create_user_table, register_user, login_user

create_user_table()

print("1. Register")
print("2. Login")
choice = input("Choose an option: ")

if choice == "1":
    register_user()
elif choice =="2":
    login_user()
else:
    print("Invalid option!")