while True:
    first_number = input("enter your first number : ")
    second_number = input("enter your secondnumber : ")

    user_choice = input("""please choice the option
    ^ for double
    + for addition
    - for subtraction 
    """)
    if user_choice == "^":
        print("double = ", first_number)
    elif user_choice == "+":
        print("addition = ", first_number + second_number) 
    else:
        print("subtraction= ", first_number - second_number)
        print("invalid option")
        
        user_choice = input("""
        do you want to continue?
        yes or
        no """)
        if user_choice.lower() == "no":
            break 