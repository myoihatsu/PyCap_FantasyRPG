import os
import json

#* ensure directory exists
def check_dir():
    """Checks if the characters directory exists, and creates it if not."""
    if not os.path.exists("./characters"):
        os.makedirs("./characters")

#* select option function, take int, check if within range, return int
def select_option(option_range):
    """Prompts the user to select a numerical option within a specified range.

    Args:
        option_range (int): The maximum valid option (inclusive).

    Returns:
        int: The valid option selected by the user.
    """
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
    """Saves character data into a JSON file within the characters directory.

    Args:
        name (str): The name of the character, used to name the file.
        character_data (dict): A dictionary containing character statistics.
    """
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


#* Is it okay to print and return in one function in working environment? idk
def display_existing_char():
    """Lists all characters found in the characters directory and prints them.

    Returns:
        list: A list of paths to the character JSON files found.
    """
    available_files = []
    count = 0
    for file_dir in os.listdir("./characters"):
        available_files.append("./characters/" + file_dir)
        count += 1
        print(f"{count}.{file_dir[5:-5:]}")
    return available_files


#* delete using os
def delete_character():
    """Handles the character deletion process through user input."""
    available_files = display_existing_char()
    print("Choose character to delete, insert number only:")
    to_delete = select_option(len(available_files))-1
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
    """A utility class for capturing and validating user input."""
    @staticmethod
    def get_text(context):
        """Captures a non-empty string from the user.

        Args:
            context (str): The prompt message to display.

        Returns:
            str: The text entered by the user.
        """
        while True:
            txt = input(context)
            if not txt:
                print("Err: Cannot be empty")
            else:
                return txt
    
    @staticmethod
    def get_num(context):
        """Captures a positive integer from the user.

        Args:
            context (str): The prompt message to display.

        Returns:
            int: The positive integer entered by the user.
        """
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
def get_commons_stat(unique_stat):
    """Prompts user for basic character stats common to all classes.

    Args:
        unique_stat (int): The primary attribute value for the specific class.

    Returns:
        tuple: Contains name (str), health (int), mana (int), action_speed (int), and unique_stat (int).
    """
    name = user_input.get_text("Insert Character Name: ")
    health = user_input.get_num("Insert character's initial health: ")
    mana = user_input.get_num("Insert character's initial mana: ")
    action_speed = user_input.get_num("Insert character's action_speed: ")

    return name,health,mana,action_speed,unique_stat


#* Load file
def load_json(dir):
    """Loads and decodes a JSON file.

    Args:
        dir (str): The file path to the JSON file.

    Returns:
        dict: The decoded character data, or None if an error occurs.
    """
    try:
        with open(dir,'r') as f:
            character_data = json.load(f)
            return character_data
    except FileNotFoundError:
        print("Error: The file was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file (invalid JSON format).")
    

#* Loop files in directory, use load_json(dir) to display it
def display_character():
    """Displays the stats of all characters in the characters directory."""
    for file_dir in os.listdir("./characters"):
        character_data = load_json("./characters/" + file_dir)

        if "strength" in character_data:
            primary_stat = "strength"
        elif "intelligence" in character_data:
            primary_stat = "intelligence"
        elif "finesse" in character_data:
            primary_stat = "finesse"
        
        print("==========================================")
        print(f"name: {character_data['name']}\nclass: {character_data['job_class']}\nhealth: {character_data['health']}\nmana: {character_data['mana']}\naction speed: {character_data['action_speed']}\n{primary_stat}: {character_data[primary_stat]}")
        print("==========================================")


#* List existing character to be edit, choose which stat to edit, edit
def edit_character():
    """Handles the character editing process through a menu."""
    available_files = display_existing_char()
    print("Select which character to edit:")
    selection = select_option(len(available_files))
    character_data = load_json(available_files[selection-1])
    
    if "strength" in character_data:
        primary_stat = "strength"
    elif "intelligence" in character_data:
        primary_stat = "intelligence"
    elif "finesse" in character_data:
        primary_stat = "finesse"

    print("== Edit Operation ========================")
    print(f"\nYou have chosen {character_data['name']}\nclass: {character_data['job_class']}")
    print("==========================================")
    print(f"Can be edited: \n1.health: {character_data['health']}\n2.mana: {character_data['mana']}\n3.action speed: {character_data['action_speed']}\n4.{primary_stat}: {character_data[primary_stat]}")
    print("==========================================")

    print("Which of these values you wish to edit: ")
    e_selection = select_option(4)

    match e_selection:
        case 1:
            before = character_data["health"]
            new = user_input.get_num("Insert new health amount: ")
            if before == new:
                return
            character_data["health"] = new
            rewrite_stats(available_files[selection-1],character_data)
        case 2:
            before = character_data["mana"]
            new = user_input.get_num("Insert new mana amount: ")
            if before == new:
                return
            character_data["mana"] = new
            rewrite_stats(available_files[selection-1],character_data)
        case 3:
            before = character_data["action_speed"]
            new = user_input.get_num("Insert new action speed amount: ")
            if before == new:
                return
            character_data["action_speed"] = new
            rewrite_stats(available_files[selection-1],character_data)
        case 4:
            before = character_data[primary_stat]
            new = user_input.get_num(f"Insert new {primary_stat} amount: ")
            if before == new:
                return
            character_data[primary_stat] = new
            rewrite_stats(available_files[selection-1],character_data)


#* try open the file specified, and try to rewrite
def rewrite_stats(file_to_rewrite,stat):
    """Rewrites the JSON file with updated character statistics.

    Args:
        file_to_rewrite (str): The path to the file to be updated.
        stat (dict): The updated character data.
    """
    try:
        with open(file_to_rewrite,'w') as temp:
            json.dump(stat,temp,indent=4) 
    except OSError as e:
        print(f"File Error: Could not write to disk. {e}")
    except TypeError as e:
        print(f"Data Error: Dictionary contains items that can't be JSON. {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
