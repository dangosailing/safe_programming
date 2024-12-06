from secure_operations import create_user_table, register_user, login_user, save_note, view_notes

# Make this into class instead
user_info = {"username": None, "user_id": None}

create_user_table()

menu_options = {"no_user":["1. Register", "2.Login"], "user_logged_in" : ["1. Logout", "2. Write Note", "3. View Notes"]}

while True:
    if user_info["username"] is None:
        for option in menu_options["no_user"]:     
            print(option)
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice =="2":
            user_info = login_user()
            print(user_info)
        else:
            print("Invalid option!")
    else: 
        break
while True:
    for option in menu_options["user_logged_in"]:     
        print(option)
    choice = input(f"Welcome {user_info["username"]}! Choose an option: ")

    if choice == "1":
        print("----IMPLEMENT LOGOUT FEATURE----")
        break
    elif choice =="2":
        user_note = input("Write your note:\n")        
        save_note(user_note, user_info["user_id"])
    elif choice =="3":
        view_notes(user_info["user_id"])
    else:
        print("Invalid option!")
        