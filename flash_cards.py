# Flash Card Script
import random
import terminology

python = terminology.basic_terms


print("""\n
**** Welcome to the Flash Card exercises ****
""")

def start():
    print("\nWhat topic would you like to review?")
    print("""
    1. Python Terminology
    2. Object-Oriented Programming
    3. Exit
    """)
    flash = input("> ")
    if flash == "1":
        practice(python)

    elif flash == "2":
        import OOP_terminology

    elif flash == "3":
        import accounts
        accounts.options()

    else:
        print("I don't understand that command.")
        start()

def practice(topic):
    print("\nHow many exercises do you want?")
    number = int(input())
    for i in range(0, number):
        print('\t', random.choice(list(topic)))
    else:
        start()

start()
