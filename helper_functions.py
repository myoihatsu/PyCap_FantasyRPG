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
def delete_character():
    available_files = []
    count = 0
    for file_dir in os.listdir("./characters"):
        available_files.append("./characters/" + file_dir)
        count += 1
        print(f"{count}.{file_dir[5:-5:]}")
    
    print("Choose character to delete, insert number only:")
    to_delete = select_option(count)-1
    while True:
        confirmation = user_input.get_text("Are you sure? Y or N: ")
        if confirmation.lower() == "y":        
            if os.path.exists(available_files[to_delete]):
                os.remove(available_files[to_delete])
                print("Character json deleted successfully")
                break
            else:
                print("Err: File doesn't exist.")
        elif confirmation.lower() == "n":
            break
        else:
            print("err: Insert Y / y for Yes or N / n for No")
            continue


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
            try:
                num = int(num)
                if num <= 0:
                    print("Err: Value must be positive")
                    continue
                return num
            except ValueError:
                print("Err: Must contain numbers only")

#* functions to get common values of a character-based object for initialization
#* primary stats (STR,INT,FIN aka unique_stat) are passed using diff_stat
#* why? just for testing if it works that's all, but I'm keeping this
def get_commons(unique_stat):
    name = user_input.get_text("Insert Character Name: ")
    health = user_input.get_num("Insert character's initial health: ")
    mana = user_input.get_num("Insert character's initial mana: ")
    action_speed = user_input.get_num("Insert character's action_speed: ")

    return name,health,mana,action_speed,unique_stat


#* Load file
def load_json(dir):
    try:
        with open(dir,'r') as f:
            character_data = json.load(f)
            return character_data
    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file (invalid JSON format).")
    

#* Loop files in directory, use load_json(dir) to display it
def display_character():
    for file_dir in os.listdir("./characters"):
        character_data = load_json("./characters/" + file_dir)

        if "strength" in character_data:
            primary_stat = "strength"
        if "intelligence" in character_data:
            primary_stat = "intelligence"
        if "finesse" in character_data:
            primary_stat = "finesse"
        
        print("==========================================")
        print(f"name: {character_data["name"]}\nclass: {character_data["job_class"]}\nhealth: {character_data["health"]}\nmana: {character_data["mana"]}\naction speed: {character_data["action_speed"]}\nstrength: {primary_stat}")
        print("==========================================")