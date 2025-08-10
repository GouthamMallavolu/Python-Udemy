# Caeser Cipher

def encrypt(input_text, input_shift):
    list_text = []
    for i in input_text:
        list_text.append(i)
    for i in range(len(list_text)):
        for j in range(1, input_shift + 1):
            if ord(list_text[i]) < 97:
                continue
            elif ord(list_text[i]) + 1 > 122:
                list_text[i] = chr(97)
            else:
                list_text[i] = chr(ord(list_text[i]) + 1)
    text = ""
    for i in list_text:
        text += i
    print(f"Encrypted text : {text}")
    print("\n+++++++++++++++++++++++++++++\n")

def decrypt(input_text, input_shift):
    list_text = []
    for i in input_text:
        list_text.append(i)
    for i in range(len(list_text)):
        for j in range(1, input_shift + 1):
            if ord(list_text[i]) < 97:
                continue
            elif ord(list_text[i]) - 1 < 97:
                list_text[i] = chr(122)
            else:
                list_text[i] = chr(ord(list_text[i]) - 1)
    text = ""
    for i in list_text:
        text += i
    print(f"Decrypted text : {text}")
    print("\n+++++++++++++++++++++++++++++\n")


print(""" ________  ________  _______   ________  _______   ________          ________      ___    ___ ________  ___  ___  _______   ________     
|\   ____\|\   __  \|\  ___ \ |\   ____\|\  ___ \ |\   __  \        |\   ____\    |\  \  /  /|\   __  \|\  \|\  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \|\  \ \   __/|\ \  \___|\ \   __/|\ \  \|\  \       \ \  \___|    \ \  \/  / | \  \|\  \ \  \\\  \ \   __/|\ \  \|\  \   
 \ \  \    \ \   __  \ \  \_|/_\ \_____  \ \  \_|/_\ \   _  _\       \ \  \        \ \    / / \ \   ____\ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \____\ \  \ \  \ \  \_|\ \|____|\  \ \  \_|\ \ \  \\  \|       \ \  \____    \/  /  /   \ \  \___|\ \  \ \  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\ \__\ \_______\____\_\  \ \_______\ \__\\ _\        \ \_______\__/  / /      \ \__\    \ \__\ \__\ \_______\ \__\\ _\ 
    \|_______|\|__|\|__|\|_______|\_________\|_______|\|__|\|__|        \|_______|\___/ /        \|__|     \|__|\|__|\|_______|\|__|\|__|
                                 \|_________|                                    \|___|/                                                 \n""")

while(True):
    selection = input("You want to encrypt or decrypt ? ").lower()
    if selection == "encrypt":
        input_text = input("enter text to encrypt : ")
        input_shift = int(input("enter shifter : "))
        encrypt(input_text, input_shift)
    elif selection == "decrypt":
        input_text = input("enter text to decrypt : ")
        input_shift = int(input("enter shifter : "))
        decrypt(input_text, input_shift)
    else:
        print("\n INVALID CHOICE ! ")
        print("\n+++++++++++++++++++++++++++++\n")
