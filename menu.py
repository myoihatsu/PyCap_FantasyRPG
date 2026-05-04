from helper_functions import *
from char_creation import *
import sys

def display_menu():
    print("==========================================")
    print("Welcome to FantasyRPG battler")
    print("==========================================")
    print("== Menu ==================================")
    print("1. Display available characters")
    print("2. BATTLEEEEE!")
    print("3. Add new character")
    print("4. Delete a character")
    print("5. Edit a character")
    print("6. Exit")
    print("==========================================")

    selection = select_option(6)

    match selection:
        case 1:
            display_character()
        case 2:
            ...
        case 3:
            choose_class()
        case 4:
            ...
        case 5:
            ...
        case 6:
            sys.exit()