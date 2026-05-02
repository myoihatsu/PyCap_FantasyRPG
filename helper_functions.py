import os
import json

#* select option function, take int, check if within range, return int
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


#* save character creation to a new file .json format and create new file
def save_character(name,character_data):
    new_file = "./characters/" + "char_" + name +".json"
    try:
        with open(new_file,'w') as temp:
            json.dump(character_data,temp,indent=4)

    #* I copy from online for exception. 
    except OSError as e:
        print(f"File Error: Could not write to disk. {e}")
    except TypeError as e:
        print(f"Data Error: Dictionary contains items that can't be JSON. {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


#* delete using os
def delete_character(file_path):
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Character json deleted successfully")
    else:
        print("Err: File doesn't exist.")

Sauron = {
    "name":"Sauron",
    "HP" : 50
}

save_character("Sauron",Sauron)
delete_character("./characters/char_Sauron.json")
