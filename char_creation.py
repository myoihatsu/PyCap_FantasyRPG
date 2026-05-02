from job_class import *

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


#*Move to helper functions later

def select_option(option_range):
    option_range = option_range + 1

    while True:    
        selection = input("Select option: ")
        
        try:
            selection = int(selection)
        except ValueError:
            print("Err: Insert numerical value only")
            continue

        if selection not in range(1,option_range):
            print("Err: Out of range.")
        else:
            return selection

choose_class()
