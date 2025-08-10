#coffee Machine

# import os
import time
import datetime
import pwinput as pwinput

machine_logo = """
█▀▀ █▀█ █▀▀ █▀▀ █▀▀ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
█▄▄ █▄█ █▀░ █▀░ ██▄ ██▄   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄\n"""

maintenance_logo = '''
█▀▄▀█ ▄▀█ █ █▄░█ ▀█▀ █▀▀ █▄░█ ▄▀█ █▄░█ █▀▀ █▀▀
█░▀░█ █▀█ █ █░▀█ ░█░ ██▄ █░▀█ █▀█ █░▀█ █▄▄ ██▄\n'''

customer_logo = '''
█▀▀ █░█ █▀ ▀█▀ █▀█ █▀▄▀█ █▀▀ █▀█
█▄▄ █▄█ ▄█ ░█░ █▄█ █░▀░█ ██▄ █▀▄\n'''

# os.system('cls')


def encrypt(passs, shifter):
    list_text = []
    for i in passs:
        list_text.append(i)
    for i in range(len(list_text)):
        for j in range(1, shifter + 1):
            if ord(list_text[i]) < 97:
                continue
            elif ord(list_text[i]) + 1 > 122:
                list_text[i] = chr(97)
            else:
                list_text[i] = chr(ord(list_text[i]) + 1)
    text = ""
    for i in list_text:
        text += i
    return text


Ingredients = {
    "water": 200,
    "coffee": 200,
    "milk": 200,
    "money": 0
}

maintain = {
    "username": "Maintenance",
    "Password": "pdlqwhqdqfh"
}

ITEMS = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20,
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    },
    "hotwater": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 0,
        },
        "cost": 5,
    }
}

machine = "ON"


def printIn():
    print(f"\nThe machine report at {datetime.datetime.now()}\n================\nWater = {Ingredients['water']} ml\n", end="")
    print(f"Milk = {Ingredients['milk']} ml\nCoffee = {Ingredients['coffee']} ml\nMoney = {Ingredients['money']} INR")


def add_ingredients():
    Ingredients['water'] += int(input("\nAdd water quantity : "))
    Ingredients['milk'] += int(input("Add milk quantity : "))
    Ingredients['coffee'] += int(input("Add coffee quantity : "))
    print("\nIngredients added successfully")


def check_ingredients(selection):
    r = 0
    if Ingredients['milk'] >= ITEMS[selection]['ingredients']['milk']:
        if Ingredients['coffee'] >= ITEMS[selection]['ingredients']['coffee']:
            if Ingredients['water'] >= ITEMS[selection]['ingredients']['water']:
                if money_insert >= ITEMS[selection]['cost']:
                    print("\nMoney received, please wait while your delicious coffee being prepared\n")
                    Ingredients['milk'] -= ITEMS[selection]['ingredients']['milk']
                    Ingredients['coffee'] -= ITEMS[selection]['ingredients']['coffee']
                    Ingredients['water'] -= ITEMS[selection]['ingredients']['water']
                    Ingredients['money'] += ITEMS[selection]['cost']
                    r = 1
    if r == 1:
        return True
    else:
        return False


def preparation():
    print("\n[", end="")
    for i in range(20):
        time.sleep(1)
        print("|", end="")
    print("]\n")


while machine == "ON":
    W_Pass = 0
    s = 0
    print("\n")
    print(machine_logo)
    user = input("==========================\n\nplease select the user customer/maintenance : ")
    if user == "maintenance":
        # os.system('cls')
        print(maintenance_logo)
        while W_Pass != 3 and machine == 'ON' and s != 1:
            username = input("\nenter Username : ")
            password = pwinput.pwinput(prompt="enter Password : ", mask='*')
            if username == maintain["username"] and encrypt(password, 3) == maintain["Password"]:
                print("login success")
                c = 0
                while c != 1:
                    select_main = input("\nList of Operations\nReport/Turnoff_machine/Add_ingredients/Exit\n: ").lower()
                    if select_main == 'report':
                        printIn()
                    elif select_main == 'turnoff_machine':
                        machine = 'OFF'
                        print("\nMachine turned off successfully ! Bye !!\n")
                        break
                    elif select_main == 'add_ingredients':
                        add_ingredients()
                    elif select_main == 'exit':
                        c, s = 1, 1
                    else:
                        print("\nInvalid selection\n")
            else:
                W_Pass += 1
                print("INVALID username/password")
    if W_Pass == 3:
        print("\nEntered the INVALID username/password for continuous 3 times and the machine is locked")
        for i in range(3):
            # os.system('cls')
            print(f"\nMachine will unlock in {W_Pass} seconds")
            time.sleep(1)
            W_Pass -= 1
        print("\nMachine Unlocked")

    elif user == "customer":
        # os.system('cls')
        print(customer_logo)
        print(f"\nAvailable MENU\n=============\nEspresso - {ITEMS['espresso']['cost']} INR", end="")
        print(f"\nLatte - {ITEMS['latte']['cost']} INR\nCappuccino - {ITEMS['cappuccino']['cost']} INR", end="")
        print(f"\nHotWater - {ITEMS['hotwater']['cost']} INR\n")
        user_select = input("please Select : ").lower()
        money_insert = int(input("Please enter the money in INR : "))
        if user_select == 'espresso' or user_select == 'latte' or user_select == 'cappuccino' or user_select == 'hotwater':
            if check_ingredients(user_select):
                preparation()
                if money_insert == ITEMS[user_select]['cost']:
                    print("\nYour coffee is prepared ! enjoy !!\n")
                else:
                    print("\nYour coffee is prepared ! enjoy !!\n")
                    print(f"And don't forget to collect change {money_insert - ITEMS[user_select]['cost']} INR\n")
            else:
                print("""\nOops! there are insufficient ingredients at the moment in the machine (or) 
                Money is insufficient for the selected choice\nPlease collect your money""")
        else:
            print("\nINVALID menu selection\n")
