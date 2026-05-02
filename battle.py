# from char_creation import * #* not in use for now
from job_class import *

#! for now just use some job_class directly to create char for test

king = Grunt("Aragorn",120,10,0.9,10)
villain = Wizard("Saruman",90,60,0.5,15)

def first_move(char_one,char_two):
    ...

def battle(char_one,char_two):

    #! I explicitly nerfed char one damage as char one would be king(Grunt)
    #! currently Grunt Class damage too op
    c1_dmg = (char_one.get_damage()) * 0.2
    c2_dmg = (char_two.get_damage()) * 0.45
    c1_name = char_one._name
    c2_name = char_two._name
    c1_hp = char_one._health
    c2_hp = char_two._health
    c1_ac_spd = char_one._action_speed
    c2_ac_spd = char_two._action_speed
    round = 1


    #* bad design, but at least it works for now, will refactor later
    while c1_hp > 0 or c2_hp > 0 :
        if c1_ac_spd > c2_ac_spd:
            #c1 attack
            print(f"==== ROUND {round} ")
            print(f"{c1_name} dealt {c1_dmg} damage to {c2_name}")
            c2_hp -= c1_dmg
            print(f"{c1_name} HP: {c1_hp}")
            print(f"{c2_name} HP: {c2_hp}")
            if c2_hp < 0:
                print("\n\n")
                print("======== WINNER ========")
                print(f"{c1_name}")
                break
            
            #c2 attack
            print(f"{c2_name} counter attacked. dealt {c2_dmg} to {c1_name}")
            c1_hp -= c2_dmg
            print(f"{c1_name} HP: {c1_hp}")
            print(f"{c2_name} HP: {c2_hp}")
            if c1_hp < 0:
                print("\n\n")
                print("======== WINNER ========")
                print(f"{c2_name}")
                break
            
            print(f"END OF ROUND {round} ====")
            print("\n\n")
            round += 1

        else:
            #c2 attack
            print(f"==== ROUND {round} ")
            print(f"{c2_name} dealt {c2_dmg} damage to {c1_name}")
            c1_hp -= c2_dmg
            print(f"{c2_name} HP: {c2_hp}")
            print(f"{c1_name} HP: {c1_hp}")
            if c1_hp < 0:
                print("\n\n")
                print("======== WINNER ========")
                print(f"{c2_name}")
                break

            #c1 attack
            print(f"{c1_name} counter attacked. dealt {c1_dmg} to {c2_name}")
            c2_hp -= c1_dmg
            print(f"{c2_name} HP: {c2_hp}")
            print(f"{c1_name} HP: {c1_hp}")
            if c2_hp < 0:
                print("\n\n")
                print("======== WINNER ========")
                print(f"{c2_name}")
                break

            print(f"END OF ROUND {round} ====")
            print("\n\n")
            round += 1

battle(king,villain)