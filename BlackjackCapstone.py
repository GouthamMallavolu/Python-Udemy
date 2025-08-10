#Blackjack Capstone Project

import random
import os

logo = """
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

░█████╗░░█████╗░██████╗░░██████╗████████╗░█████╗░███╗░░██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔════╝
██║░░╚═╝███████║██████╔╝╚█████╗░░░░██║░░░██║░░██║██╔██╗██║█████╗░░
██║░░██╗██╔══██║██╔═══╝░░╚═══██╗░░░██║░░░██║░░██║██║╚████║██╔══╝░░
╚█████╔╝██║░░██║██║░░░░░██████╔╝░░░██║░░░╚█████╔╝██║░╚███║███████╗
░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝╚══════╝\n"""

os.system('cls')
print(logo)
cards = ['A', 'J', 'K', 'Q', 2, 3, 4, 5, 6, 7, 8, 9, 10]
human_selection = []
computer_selection = []
Ace_select = [1, 11]


def convert(human_selection, computer_selection):
    for i in range(len(human_selection)):
        if human_selection[i] == 'J' or human_selection[i] == 'K' or human_selection[i] == 'Q':
            human_selection[i] = 10
    for i in range(len(computer_selection)):
        if computer_selection[i] == 'J' or computer_selection[i] == 'K' or computer_selection[i] == 'Q':
            computer_selection[i] = 10
        elif computer_selection[i] == 'A':
            computer_selection[i] = random.choice(Ace_select)
    return human_selection, computer_selection


def printing(human_selection, computer_selection):
    print(f"The cards are drawn. Player has cards {human_selection}\nand\nDealer has a cards [{computer_selection[0]}, ....]")


def player(h):
    c = 0
    for i in h:
        if i == 'A':
            select_i = int(input("\nPlease choose if you want this 'A' card to be added as 1 or 11 ? : "))
            c += select_i
        else:
            c += i
    return c


def dealer(c):
    s = 0
    for i in c:
        s += i
    return s


select = input("\nDo you want to start the game ? Type 'Yes' or 'No' : ").lower()

if select == 'yes':
    os.system('cls')

    for i in range(2):
        human_selection.append(random.choice(cards))
        computer_selection.append(random.choice(cards))
    printing(human_selection, computer_selection)

    while(True):
        select_x = input("\nWant to draw another card ? Type 'Yes' or 'No' : ").lower()
        if select_x == 'yes':
            os.system('cls')
            human_selection.append(random.choice(cards))
            printing(human_selection, computer_selection)
        else:
            human_selection, computer_selection = convert(human_selection, computer_selection)
            break

    total_h = player(human_selection)
    total_c = dealer(computer_selection)

    while total_h <= 16 or total_c <= 16:
        if total_h <= 16:
            select_y = input("\nOops the sum added is not more than 16 you must select another card !! Type 'Yes' to select or 'No' to exit : ").lower()
            if select_y == 'yes':
                os.system('cls')
                human_selection.append(random.choice(cards))
                printing(human_selection, computer_selection)
            else:
                break
        if total_c <= 16:
            print("\nDealer choose another card as he's total sum is less than or equal to 16 !!!\n")
            computer_selection.append(random.choice(cards))

        human_selection, computer_selection = convert(human_selection, computer_selection)
        total_h = player(human_selection)
        total_c = dealer(computer_selection)

    if total_h > 16 and total_c > 16:
        if 21 >= total_h > total_c:
            print(f"\nYou WON with total of {total_h} and with cards {human_selection},\nwhich are more than dealer total of {total_c} and with cards {computer_selection}\n")
        elif 21 >= total_c > total_h:
            print(f"\nDealer WON with total of {total_c} and with cards {computer_selection},\nwhich are more than player total of {total_h} and with cards {human_selection}\n")
        elif (total_h > 21 and total_c > 21) or total_c == total_h:
            print(f"\nGAME DRAW \nPlayer: Total = {total_h} and cards = {human_selection}\nDealer: Total = {total_c} and cards = {computer_selection}\n")
        elif total_c > 21:
            print(f"\nYou WON with total of {total_h} and with cards {human_selection},\nwhere dealer has total of {total_c} which is more than allowed total '21', with cards {computer_selection}\n")
        elif total_h > 21:
            print(f"\nDealer WON with total of {total_c} and with cards {computer_selection},\nwhere player has total of {total_h} which is more than allowed total '21', with cards {human_selection}\n")

    else:
        print("\nThanks for playing !!!\n")

else:
    print(f"\n!!! HAVE A GREAT DAY !!!!")
