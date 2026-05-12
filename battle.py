from job_class import *
from helper_functions import *
import random

def first_move(char_one,char_two):
    """Determines the turn order based on action speed rolls.

    Each character rolls a random integer between 1 and their action_speed. 
    The higher roll moves first. In the event of a tie, a random choice 
    is made to determine the starter.

    Args:
        char_one (dict): The first character dictionary.
        char_two (dict): The second character dictionary.

    Returns:
        tuple[dict, dict]: A tuple containing (attacker, target) in the 
            determined turn order.
    """

    roll_one = random.randint(1,max(1,char_one["action_speed"]))
    roll_two = random.randint(1,max(1,char_two["action_speed"]))

    if roll_one > roll_two:
        return char_one, char_two
    elif roll_two > roll_one:
        return char_two, char_one
    else:
        winner = random.choice([1,2])
        if winner == 1:
            return char_one,char_two
        else:
            return char_two,char_one

#* damage updates every turn for Grunt and Wizard, Ranger stays the same since action speed is static
def get_damage(character) -> float: 
    """Calculates combat damage based on class-specific stat scaling.

    Args:
        character (dict): A dictionary containing "job_class" and the secondary 
            scaling stats like "strength", "health", "intelligence", "mana", 
            "finesse", or "action_speed".

    Returns:
        float: The calculated damage rounded to 2 decimal places, or 0.0 if the 
            class is unrecognized.
    """
    if character["job_class"] == "Grunt":
        return round(character["strength"] + 0.15 * character["health"], 2)
    if character["job_class"] == "Wizard":
        return round(character["intelligence"] + 0.7 * character["mana"], 2)
    if character["job_class"] == "Ranger":
        return round(character["finesse"] + 0.8 * character["action_speed"], 2)
    
    return 0.0


#* attack
def attack(attacker,target,mode=0) -> bool:
    """Executes a combat turn including damage calculation and resource management.

    Args:
        attacker (dict): A dictionary containing 'name', 'health', 'mana', and stats for get_damage.
        target (dict): A dictionary containing 'name', 'health', and 'mana' of the opponent.
        mode (int, optional): The combat stance. 0 for normal attack, 1 for counter attack. Defaults to 0.

    Returns:
        bool: True if either the attacker or target has been defeated (HP <= 0), False otherwise.
    """

    attacker_name = attacker["name"]

    damage = get_damage(attacker)

    target_name = target["name"]

    #*0 for attack, 1 for counter attack
    if mode == 0:
        if attacker["mana"] >= 4:
            print(f"{attacker_name} dealt {damage} damage to {target_name}")
            attacker["mana"] -= 4
            target["health"] -= damage
        else:
            struggle_damage = round(damage * 0.7, 2)
            print(f"{attacker_name} out of mana. {attacker_name} struggled and dealt {struggle_damage} damage at the cost of 4 HP")
            attacker["health"] -= 4
            target["health"] -= struggle_damage
    if mode == 1:
        if attacker["mana"] >= 4:
            print(f"{attacker_name} counter attacked dealt {damage} damage to {target_name}")
            attacker["mana"] -= 4
            target["health"] -= damage
        else:
            struggle_damage = round(damage * 0.7, 2)
            print(f"{attacker_name} counter attacked, but out of mana. {attacker_name} struggled and dealt {struggle_damage} damage at the cost of 4 HP")
            attacker["health"] -= 4
            target["health"] -= struggle_damage
            
    
    print(f"{attacker_name} HP: {round(attacker['health'], 2)} MP: {round(attacker['mana'], 2)}")
    print(f"{target_name} HP: {round(target['health'], 2)} MP: {round(target['mana'], 2)}")

    print("")
    input("Press Enter to continue")

    #check if HP = or less than 0
    if target["health"] <= 0:
        return True
    if attacker["health"] <= 0:
        return True
    
    return False

def battle(char_one,char_two):
    """Orchestrates a turn-based combat loop between two characters.

    Each round consists of an initiative roll to determine the first attacker, 
    an initial attack phase, and a subsequent counter-attack phase. The loop 
    continues until one character's health drops to zero or below.

    Args:
        char_one (dict): The first combatant dictionary.
        char_two (dict): The second combatant dictionary.
    """

    round = 1
    while True:
        print(f"\n=== Round {round} ===")

        #deciding first to move
        attacker, target = first_move(char_one,char_two)

        print(f"=== {attacker["name"]} rolls higher, they get to move first !")

        #start attacking
        #check if it return True and attacking at the same time, this is deliberate :D
        if attack(attacker,target):
            print("\n\n======== WINNER ========")
            if target["health"] <=0:
                print(f"{attacker["name"]}\n\n")
            else:
                print(f"{target["name"]} won. {attacker["name"]} struggled to death\n\n")
            break

        print("\n")

        #counter-attacking
        if attack(target,attacker,1):
            print("\n\n======== WINNER ========")
            if target["health"] <=0:
                print(f"{attacker["name"]}\n\n")
            else:
                print(f"{target["name"]} won. {attacker["name"]} struggled to death\n\n")
            break
        
        print(f"=== End of Round {round} ===\n")
        round += 1


#* display available character , display_existing_char(), return list of dir
#* select_option -1 = index for selecting dir in available_character
#* load_json , load the dict containing stats of characters       
def choose_character_to_battle():
    """Handles the selection process for two unique characters and starts a battle.

    Prompts the user to select two characters from the available list. Includes 
    validation logic to ensure the same character cannot be selected twice 
    against itself. Once two distinct characters are chosen, their data is 
    loaded and the battle sequence is initiated.
    """
    
    print("==========================================")
    print("Select first character to battle: ")
    available_character = display_existing_char()

    #character one selection
    selected_one = select_option(len(available_character))
    selected_one -= 1
    character_one = load_json(available_character[selected_one])

    print("Select second character to battle: ")
    while True:
        #character two selection
        selected_two = select_option(len(available_character))
        selected_two -= 1

        #check if selected character two is the same as one
        if selected_two == selected_one:
            print("Err: Second character cannot be the same as character one.")
        else:
            character_two = load_json(available_character[selected_two])
            break
    
    battle(character_one,character_two)