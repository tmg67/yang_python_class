# number guessing game
import random
random_number = random.randint(1,100)
# print (random_number)
while True:
    user_guess = int(input("enter a guess"))
    if user_guess == random_number:
        print(" you win ")
        break
    elif user_guess< random_number:
        print("too low")
    else:
        print("too high")
