from job_class import Grunt, Wizard, Ranger
from helper_functions import user_input, get_commons_stat, save_character, select_option

#*Display options, call select option and char_creation
def choose_class() -> None:
    """Displays class selection menu and initiates character creation."""
    print(
        "==========================================\n"
        "Choose your character's class (number only)\n"
        "1. Grunt\n"
        "2. Wizard\n"
        "3. Ranger\n"
        "==========================================\n"
        )
    
    options: int = select_option(3)
    char_creation(options)


#* Choose class function.
def char_creation(selection: int) -> None:
    """Creates a new character based on the selected class.

    Args:
        selection (int): The integer representing the chosen class (1-3).
    """
    match selection:
        case 1:
            print("Grunt class uses Strenght(STR) and a portion of HP as damage")
            stat: int = user_input.get_num("Insert character's STR: ")
            #* Note for self, * used to unpack tuple from 'return'
            new_char: dict = Grunt(*get_commons_stat(stat)).to_dict()
            save_character(new_char["name"], new_char)
        case 2:
            print("Wizard class uses Intelligence(INT) and a portion of MP as damage")
            stat: int = user_input.get_num("Insert character's INT: ")
            new_char: dict = Wizard(*get_commons_stat(stat)).to_dict()
            save_character(new_char["name"], new_char)
        case 3:
            print("Ranger class uses Finesse(FIN) and a portion of HP and MP as damage")
            stat: int = user_input.get_num("Insert character's FIN: ")
            new_char: dict = Ranger(*get_commons_stat(stat)).to_dict()
            save_character(new_char["name"], new_char)
