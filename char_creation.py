from job_class import *


def choose_class():
    print(
        "==========================================\n"
        "1. Grunt\n"
        "2. Wizard\n"
        "3. Ranger\n"
        "==========================================\n"
        )
    
    while True:
        
        selection = input("Choose your class, insert number only: ")
        
        try:
            selection = int(selection)
        except ValueError:
            print("Err: Insert numerical value only")
            continue

        if selection not in range(1,3+1):
            print("Err: Out of range.")
        else:
            
            break

def char_creation(job_class):
    ...


choose_class()
