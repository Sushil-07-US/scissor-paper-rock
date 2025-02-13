# Second project

# Scissor, Paper and Rock game:

import random

choices = ("scissor", "paper", "rock")
ram_choice = random.choice(choices)

attempts = 5
att_count = 1

print("Are you ready to play Scissors, Paper and Rock")

ques =input ("Type Y for Yes and N for NO: ").lower()

if ques == "y" or ques =="yes":

    game = input("choose scissor, paper and rock: ").lower()

   

    

    while att_count != attempts:
        ram_choice = random.choice(choices)
        if game not in choices:
            print("Please enter valid input")
            break
            



        elif ram_choice == game:
            print(f"Computer: {ram_choice}\nYou: {game}")
            print("Tie")


        elif (ram_choice == "scissor" and game == "paper") or\
            (ram_choice == "paper" and game == "rock") or\
            (ram_choice == "rock" and game == "scissor" ) :
                
            print (f"Computer: {ram_choice}\nYou: {game}\nYou lose!")

    
        else:
            print(f"Computer: {ram_choice}\nYou: {game}\nYou Won!")
            break

        print(f"Attempt Used: {att_count} \5")
        game = input("choose scissor, paper and rock: ").lower()


        att_count+=1

else:
    print("Invalid Input! You are out of game")

print("See You Again...")

    





