# rock paper and scissors

'''
reference for code:
rock --------> 1
paper --------> -1
scissors --------> 0

Controls:
Type "r" or "R" if you want to choose "Rock"
Type "p" or "P" if you want to choose "Paper"
Type "s" or "S" if you want to choose "Scissors"

'''

import random


while True:
    system = random.choice([-1, 0, 1])

    userstring = input("Enter your choice (r/p/s): ").lower()
    userDictionary = {"r": 1, "p": -1, "s": 0}
    reverseDictionary = {1 : "Rock", -1 : "Paper", 0 : "Scissors"}

    if userstring not in userDictionary:
        print("Invalid choice! Enter r, p, or s.")
        exit()

    user = userDictionary[userstring] 

    print(f"You chose {reverseDictionary[user]} \n Computer chose {reverseDictionary[system]}")

    if(system == user):
        print("Its a Draw!")

    else:
        if(system == 1 and user == -1):
            print("You Won!")

        elif(system == 1 and user == 0):
            print("You Lose!")

        elif(system == -1 and user == 1):
            print("You Lose!")
            
        elif(system == -1 and user == 0):
            print("You Won!")   

        elif(system == 0 and user == 1):
            print("You Won!")

        elif(system == 0 and user == -1):
            print("You Lose!")

        else:
            print("Oops! There's an error occured.")   

        play_again = input("Play Again? (y/n) : ").lower()
        if play_again != "y":
            print("Thanks for Playing!")
            break


     

        
    




