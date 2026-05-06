from job_class import *
from helper_functions import *
import random
import time

def first_move(char_one,char_two):
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
def get_damage(character):
    if character["job_class"] == "Grunt":
        return character["strength"] + 0.15 * character["health"]
    if character["job_class"] == "Wizard":
        return character["intelligence"] + 0.7 * character["mana"]
    if character["job_class"] == "Ranger":
        return character["finesse"] + 0.8 * character["action_speed"]


#* attack
def attack(attacker,target,mode=0):
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
            print(f"{attacker_name} out of mana. {attacker_name} struggled and dealt {damage * 0.7} damage at the cost of 4 HP")
            attacker["health"] -= 4
            target["health"] -= damage * 0.7
    if mode == 1:
        if attacker["mana"] >= 4:
            print(f"{attacker_name} counter attacked dealt {damage} damage to {target_name}")
            attacker["mana"] -= 4
            target["health"] -= damage
        else:
            print(f"{attacker_name} counter attacked, but out of mana. {attacker_name} struggled and dealt {damage*0.7} damage at the cost of 4 HP")
            attacker["health"] -= 4
            target["health"] -= damage * 0.7
            
    
    print(f"{attacker_name} HP: {attacker["health"]} MP: {attacker["mana"]}")
    print(f"{target_name} HP: {target["health"]} MP: {target["mana"]}")

    print("")
    input("Press Enter to continue")

    #check if HP = or less than 0
    if target["health"] <= 0:
        return True
    if attacker["health"] <= 0:
        return True
    
    return False

def battle(char_one,char_two):
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