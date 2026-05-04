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


#* functions to get input
class user_input:
    @staticmethod
    def get_text(context):
        while True:
            txt = input(context)
            if not txt:
                print("Err: Cannot be empty")
            else:
                return txt
    
    @staticmethod
    def get_num(context):
        while True:
            num = input(context)
            if not num.isnumeric() or int(num) <= 0:
                print("Err: Number must be a whole number and cannot be left empty")
            else:
                num = int(num)
                return num
            

test1= user_input.get_text("Bro insert text: ")
test2= user_input.get_num("insert num bro: ")