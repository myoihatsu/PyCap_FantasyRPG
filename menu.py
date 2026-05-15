from helper_functions import *
from char_creation import *
from battle import *
import sys
import os

def display_menu():
    """Displays the main menu and handles user selection for game operations."""
    check_dir()
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

    #* Check if there are enough characters before proceeding
    char_count = len(os.listdir("./characters"))
    if selection in [1, 4, 5] and char_count < 1:
        print("No character available, create more!")
        return
    elif selection == 2 and char_count < 2:
        print("At least two characters are required to battle! Create more.")
        return

    match selection:
        case 1:
            display_character()
        case 2:
            choose_character_to_battle()
        case 3:
            choose_class()
        case 4:
            delete_character()
        case 5:
            edit_character()
        case 6:
            sys.exit()
