first_number = float(input("enter your first number : "))
second_number = float(input("enter your second number : "))

temperature_length_currency = input("""please choice the option
t for temperature
l for length
C for currency
""")

if temperature_length_currency == "t":
    print(" t = ", first_number * (9/5) + 32)
elif temperature_length_currency == "l":
    print(" l = ", first_number / second_number) 
else:
    print(" C = ", first_number * second_number)
    print("invalid option")