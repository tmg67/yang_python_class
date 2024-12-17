#number properties checker
while True:
    user_number = int(input("enter a number"))
 if user_number % 2 == 0 : # % detremines reminder
        print(f"{user_number} is odd")
else:
        print(f"{user_number} is even")

    #check prime number

    for i in range(2, user_number):
        if user_number % i == 0 :
        print(f"{user_number} is prime")
        break
        else:
        print(f"{user_number} is not prime")

    # check multiple of another number

for i in range(1, user_number):
        if i*i == user_number:
        print(f"{user_number} is a square number")
        break
 else:
        print(f"{user_number} is not a square number")

    user_choice = input("""
    do you want to continue?
    yes or
    no """)
    if user_choice.lower() == "no":
        break