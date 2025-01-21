
import random
while True:
    player1 = input("enter your choose rock/papaer/scissor ")
    player2 = input("enetr your choose rock/paper/scissor ")

    # to track the score
    score = 0

    if player1 == player2:
        print("its a tieee")
    elif player1 == "paper":
        if player2 == "scissor":
            print("you won")
            score += 1 
        else:
           print(" you lost")
    elif player1 == "scissor":
        if player2 == "rock":
            print("you won")
            score += 1
        else:
            print("you lost")
    elif player1 == "rock":
        if player2 == "scissor":
            print("you won")
            score += 1
        else:
            print("you lost")
         

        choice = input("will you like to play again yes/no:").strip()
        if choice == "no":
            print("thank you for playing")
            break 
            