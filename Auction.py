#Auction bidding using dictionaries

import os

print("""                     _   _             
     /\             | | (_)            
    /  \  _   _  ___| |_ _  ___  _ __  
   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
  / ____ \ |_| | (__| |_| | (_) | | | |
 /_/    \_\__,_|\___|\__|_|\___/|_| |_|
                                       
                                       """)

def selectHighBidder(dict_key):
    c = 0
    for i in dict_key:
        if dict_key[i] > c:
            c = dict_key[i]
            s = i
    print(f"\nThe highest bidder is '{s}' with bid amount ${c}.\n!!! Congratulations, item sold to '{s}'. !!!")


print("+=+=+=+= Welcome to auction +=+=+=+= \n")
dict_key = {}
key = input("please enter your name : ")
dict_key[key] = int(input("enter the bid amount : $"))
choice = input("Are there any other bidders ? Type 'Yes' or 'No' : ").lower()

while choice == 'yes':
    os.system('cls')
    key = input("please enter your name :")
    dict_key[key] = int(input("enter the bid amount : $"))
    choice = input("Are there any other bidders ? Type 'Yes' or 'No' : ").lower()

selectHighBidder(dict_key)