accounts = open('database.txt')


def create_account():
    new_info = open('database.txt', 'a+')
    print("\nPlease enter your desired username: ")
    new_user = input('> ')

    if new_user in accounts.read():
        print("\nThat username is already taken.\n\n")
        quit()

    else:
        print("\nPlease enter your desired password: ")
        new_pass = input('> ')
        print("\nPlease confirm your password:")
        verify = input('> ')

        if new_pass == verify:
            new_info.write(f'\n{new_user}--{new_pass}')
            print("\n\t***Account successfully created!***")

        else:
            print("\nPasswords do not match.\nPlease try again.")
            create_account()

def log_in(username, password):
    check = accounts.read().strip().split()

    if f"{username}--{password}" in check:
        accounts.close()
        return True

    else:
        accounts.close()
        return False

def options():
    print("What would you like to do?")
    print("""
    1. Play a text-based adventure game
    2. Check my health figures
    3. Study with flash cards
    4. Exit
    """)
    choice = input("> ")

    if choice == "1":
        print("What would you like to play? \n(1) A Superhero game or (2) a prison-escape game?")
        game_choice = input("> ")

        if game_choice == "1":
            import hero_game
            hero_game.a_map.play()

        elif game_choice == "2":
            import adventure_text
            adventure_text.start()

    elif choice == "2":
        import Health
        Health.start()

    elif choice == "3":
        import flash_cards
        flash_cards.start()

    elif choice == "4":
        quit()

    else:
        print("I don't understand that choice.")
        options()

print("""
\t**Welcome! My name is Jarvis.**
To begin, do you already have an account?
If so, enter 1. If you need to make a new
account, please enter 0.
""")

start = input('> ')

if start == '0':
    create_account()


print("\nPlease enter your log-in information.")
username = input("\tUsername: ")
password = input("\tPassword: ")
if log_in(username, password):
    print("\n*************************************")
    print("******  Log in is successful.  ******")
    print(f"********  Welcome, {username}!  *********")
    print("*************************************\n")
    options()

else:
    print("\nLog in was unsuccessful.")
    print("Please try again.\n\n")
    quit()
