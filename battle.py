# from char_creation import * #* not in use for now
from job_class import *
import random

#! for now just use some job_class directly to create char for test

king = Grunt("Aragorn",90,10,0.9,10)
villain = Wizard("Saruman",900,60,0.5,15)


#! simple logic first, will update to rng
def first_move(char_one,char_two):
    #* update later, higher action speed, more chance to move first
    if char_one._action_speed > char_two._action_speed:
        return char_one, char_two
    elif char_one._action_speed < char_two._action_speed:
        return char_two, char_one
    else: #* randommmmm
        if random.randint(1,2) == 1:
            return char_one, char_two
        else:
            return char_two, char_one 

#* attack
def attack(attacker,target,mode=0):
    attacker_name = attacker._name
   
    damage = attacker.get_damage()

    target_name = target._name
    

    #*0 for attack, 1 for counter attack
    if mode == 0:
        print(f"{attacker_name} dealt {damage} damage to {target_name}")
    if mode == 1:
        print(f"{attacker_name} counter attacked. dealt {damage} to {target_name}")
    target._health -= damage
    print(f"{attacker_name} HP: {attacker._health}")
    print(f"{target_name} HP: {target._health}")



def battle(char_one,char_two):
   round = 1
   while True:
       print(f"=== Round {round} ===")
       attacker, target = first_move(char_one,char_two)

       attack(attacker,target)

       round += 1

       if target._health <= 0:
        print("\n\n")
        print("======== WINNER ========")
        print(f"{attacker._name}")
        break
       
       attack(target,attacker,1)

       if attacker._health <= 0:
        print("\n\n")
        print("======== WINNER ========")
        print(f"{target._name}")
        break


battle(king,villain)

