first_number = float(input("enter your first number : "))
second_number = float(input("enter your second number : "))

print("Addition = ", first_number + second_number)

first_number = float(input("enter your first number : "))
second_number = float(input("enter your second number : "))

print("Subtraction = ", first_number - second_number)

first_number = float(input("enter your first number : "))
second_number = float(input("enter your second number : "))

print("Multiplication = ", first_number * second_number)

first_number = float(input("enter your first number : "))
second_number = float(input("enter your second number : "))


user_choice = input("""please choice the option
+ for addition
- for subtraction """)
if user_choice =="+":
    print("addition = ", first_number + second_number)
elif user_choice == "-":
    print("subtraction = ", first_number - second_number)
else:
    print("invalid option")
    