from secure_operations import create_user_table, register_user, login_user, save_note, view_notes
from Session import Session

# Make this into class instead
session = Session()

create_user_table()

menu_options = {"no_user":["1. Register", "2.Login"], "user_logged_in" : ["1. Logout", "2. Write Note", "3. View Notes"]}

while True:
    if not session.logged_in: 
        for option in menu_options["no_user"]:     
            print(option)
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice =="2":
            session_info = login_user()
            if session_info["logged_in"]:
                session.set_user_login(session_info["user_id"], username=session_info["username"])
        else:
            print("Invalid option!")
    else: 
        break
while True:
    for option in menu_options["user_logged_in"]:     
        print(option)
    choice = input(f"Welcome {session.get_username()}! Choose an option: ")

    if choice == "1":
        session.username = None
        session.user_id = None
        session.logged_in = False
        break
    elif choice =="2":
        user_note = input("Write your note:\n")        
        save_note(user_note, session.get_user_id())
    elif choice =="3":
        view_notes(session.get_user_id())
    else:
        print("Invalid option!")
        