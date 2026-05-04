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


#* Choose class function.
def char_creation(selection):
    match selection:
        case 1:
            print("Grunt class uses Strenght(STR) and a portion of HP as damage")
            stat = user_input.get_num("Insert character's STR: ")
            #* Note for self, * used to unpack tuple from 'return'
            new_char = Grunt(*get_commons(stat)).to_dict()
            save_character(new_char["name"],new_char)
        case 2:
            print("Wizard class uses Intelligence(INT) and a portion of MP as damage")
            stat = user_input.get_num("Insert character's INT: ")
            new_char = Wizard(*get_commons(stat)).to_dict()
            save_character(new_char["name"],new_char)
        case 3:
            print("Ranger class uses Finesse(FIN) and a portion of HP and MP as damage")
            stat = user_input.get_num("Insert character's FIN: ")
            new_char = Ranger(*get_commons(stat)).to_dict()
            save_character(new_char["name"],new_char)

choose_class()
