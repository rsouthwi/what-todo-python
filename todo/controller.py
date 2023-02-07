import os
from time import sleep


def clear_screen():
    os.system("clear")


def display_title_bar():
    clear_screen()
    print("""

    \t*************************************
    \t**  TODO - try out this boss app   **
    \t*************************************
    """)


def get_user_choice():
    print("\n[h] See a list of commands")
    print("[1] Show Lists")
    print("[2] Edit List")
    print("[q] quit")
    return input("\nPlease enter a command: ")


def quit_ToDo():
    clear_screen()
    print("Thank you.")
    exit()


def start_app():
    clear_screen()
    # get user_name first
    # get or create db from user_name
    # load data from json file into memory
    while True:
        choice = get_user_choice()
        if choice.lower() == "q":
            quit_ToDo()

