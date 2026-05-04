from job_class import *
from helper_functions import *

#*Display options, call select option and char_creation
def choose_class():
    print(
        "==========================================\n"
        "Choose your character's class (number only)\n"
        "1. Grunt\n"
        "2. Wizard\n"
        "3. Ranger\n"
        "==========================================\n"
        )
    
    options = select_option(3)
    char_creation(options)


#* Static for now.
def char_creation(selection):
    name = user_input.get_text("Insert Character Name: ")
    health = user_input.get_num("Insert character's initial health: ")
    mana = user_input.get_num("Insert character's initial mana: ")
    action_speed = user_input.get_num("Insert character's action_speed: ")
    
    match selection:
        case 1:
            print("Grunt class uses Strenght(STR) and a portion of HP as damage")
            stat = user_input.get_num("Insert character's STR: ")
            new_char = Grunt(name,health,mana,action_speed,stat)
            save_character(name,new_char)
        case 2:
            print("Wizard class uses Intelligence(INT) and a portion of MP as damage")
            stat = user_input.get_num("Insert character's INT: ")
            new_char = Wizard(name,health,mana,action_speed,stat)
            save_character(name,new_char)
        case 3:
            print("Grunt class uses Finesse(FIN) and a portion of HP as damage")
            stat = user_input.get_num("Insert character's FOIN: ")
            new_char = Ranger(name,health,mana,action_speed,stat)
            save_character(name,new_char)

choose_class()


