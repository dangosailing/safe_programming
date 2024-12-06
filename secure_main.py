from secure_operations import create_user_table, register_user, login_user

# Make this into class instead
user_info = {"username": None, "user_id": None}

create_user_table()

menu_options = {"no_user":["1. Register", "2.Login"], "user_logged_in" : ["1. Logout", "2. Write Note"]}

while True:
    if user_info["username"] is None:
        for option in menu_options["no_user"]:     
            print(option)
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice =="2":
            user_info= login_user()
            break
        else:
            print("Invalid option!")
    
while True:
    for option in menu_options["user_logged_in"]:     
        print(option)
    choice = input(f"Welcome {user_info["username"]}! Choose an option: ")

    if choice == "1":
        print("----IMPLEMENT LOGOUT FEATURE----")
        break
    elif choice =="2":
        print("----IMPLEMENT WRITE NOTE FEATURE----")
        break
    else:
        print("Invalid option!")
        