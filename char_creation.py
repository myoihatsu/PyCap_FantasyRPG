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
    
    selection = select_option(3)
    char_creation(selection)


#* Static for now.
def char_creation(selection):
    match selection:
        case 1:
            new_char = Grunt("Gimli",100,10,0.5,15)
            print(new_char._name)
        case 2:
            new_char = Wizard("Gandalf",60,30,0.3,25)
            print(new_char._name)
        case 3:
            new_char = Ranger("Legolas",50,15,1.2,10)
            print(new_char._name)


choose_class()
