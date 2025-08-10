#Number Guessing Game

import random
import os

master_number = random.randint(1, 100)
difficulty = {'easy': 10, 'medium': 7, 'hard': 5}
global_chances = 0

logo = """
███╗  ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗          ██████╗ ██╗   ██╗███████╗ ██████╗ ██████╗██╗███╗  ██╗ ██████╗
████╗ ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗        ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██║████╗ ██║██╔════╝
██╔██╗██║██║   ██║██╔████╔██║██████╦╝█████╗  ██████╔╝        ██║  ██╗ ██║   ██║█████╗  ╚█████╗ ╚█████╗ ██║██╔██╗██║██║  ██╗
██║╚████║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗        ██║  ╚██╗██║   ██║██╔══╝   ╚═══██╗ ╚═══██╗██║██║╚████║██║  ╚██╗
██║ ╚███║╚██████╔╝██║ ╚═╝ ██║██████╦╝███████╗██║  ██║        ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║ ╚███║╚██████╔╝
╚═╝  ╚══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝         ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚══╝ ╚═════╝\n"""
os.system('cls')
print(logo)

def guess(select, chances):
    if select > master_number:
        print("\nToo High !\n===============")
        return False, chances - 1
    elif select < master_number:
        print("\nToo Low !\n===============")
        return False, chances - 1
    elif select == master_number:
        return True, chances

select_diff = input("Please select the difficulty\n'Easy' (10 attempts),\n'Medium' (7 attempts)\n'Hard' (5 attempts)\n: ").lower()

if select_diff in difficulty:
    global_chances = difficulty[select_diff]
    chances = global_chances
    for i in range(global_chances):
        print(f"\nYou have left with attempts {chances}")
        select_p = int(input("\nEnter the guessing number : "))
        output, chances = guess(select_p, chances)
        if output and chances != 0:
            print(f"\nCongrats guessed correctly you WON !! ")
            break
    if chances == 0:
        print(f"\nOops out of attempts !! Actual Number {master_number}")
else:
    print("\n!!! HAVE A GREAT DAY !!!\n")
