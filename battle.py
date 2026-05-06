from job_class import *
from helper_functions import *
import random

#! simple logic first, will update to rng
def first_move(char_one,char_two):
    #* update later, higher action speed, more chance to move first
    if char_one["action_speed"] > char_two["action_speed"]:
        return char_one, char_two
    elif char_one["action_speed"] < char_two["action_speed"]:
        return char_two, char_one
    else: #* randommmmm
        if random.randint(1,2) == 1:
            return char_one, char_two
        else:
            return char_two, char_one 


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
        print(f"{attacker_name} dealt {damage} damage to {target_name}")
    if mode == 1:
        print(f"{attacker_name} counter attacked. dealt {damage} to {target_name}")
    target["health"] -= damage
    print(f"{attacker_name} HP: {attacker["health"]}")
    print(f"{target_name} HP: {target["health"]}")


def battle(char_one,char_two):
    round = 1
    while True:
        print(f"\n=== Round {round} ===")
        attacker, target = first_move(char_one,char_two)

        attack(attacker,target)

        print("\n")
        
        if target["health"] <= 0:
            print("\n\n")
            print("======== WINNER ========")
            print(f"{attacker["name"]}")
            break
       
        attack(target,attacker,1)

        if attacker["health"] <= 0:
            print("\n\n")
            print("======== WINNER ========")
            print(f"{target["name"]}")
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