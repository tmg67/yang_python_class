import random

player1_score = 0
player2_score = 0

while True:
   
    player1 = input("enter your choice(rock, paper, scissor)")
    player2 = random.choice(["rock", "paper", "scissor"])

    print("player1 choice{player1} and player2 choice {player2}")
    
    if player1 == player2:
            print("both selected {player1} so, it's a tie.")
    elif player1 == "rock":
        if player2 == "scissor":
            print("player2 lost")
            player1_score += 1
        else:
            print("player2 won!!!!!!.")
            player2_score += 1

    elif player1 == "scissor":
        if player2 == "paper":
            print("player2 lost")
            player1_score += 1
        else:
            print("player2 won!!!!!!")
            player2_score += 1
    elif player1 == "paper":
        if player2 == "rock":
            print("player2 lost.")
            player1_score += 1
        else:
            print("player2 won!!!!!!!!!")
            player2_score += 1

    
   
    choice = input("do you want to continue yes/no")
    if choice.strip() == "no":
        print('thank you for playing')
        break
print(f"final score :  {player1_score} and {player2_score}")
    
