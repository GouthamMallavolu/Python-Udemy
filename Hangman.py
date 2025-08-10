import random
list_hangman = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
hanged = ['''
  +---+
      |
      |
      |
     ===''', '''
   +---+
   O   |
       |
       |
     ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
select_hangman = random.choice(list_hangman)
print(logo)
print(f"\n\nHint : The word is a {len(select_hangman)} letter word.")
Lives = 0
Chances = len(select_hangman) + 3
list_choice = ['_'] * len(select_hangman)
list_select = []
for i in select_hangman:
    list_select.append(i)
while(True):
    user_choice = ""
    for i in range(len(select_hangman)):
        user_choice += list_choice[i]
    if user_choice == select_hangman:
        print("YOU WON !")
        print(f"\n=============\nWord : {user_choice}\n=============")
        break
    print(f"\nWord : {user_choice}")
    choose = input("enter a letter : ").lower()
    if choose not in select_hangman:
        print(hanged[Lives])
        Lives += 1

    if Lives == 7 or Chances == 0:
        print("\nOops! Out of chances/Lives :( \nGAME OVER ! Hanged")
        print(f"\n===================\nActual Word : {select_hangman}\n===================")
        break
    else:
        for i in range(len(select_hangman)):
            if list_select[i] == choose:
                list_choice[i] = choose
    Chances -= 1