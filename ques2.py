first_number = float(input("enter your first number : "))
second_number = float(input("enter your second number : "))
third_number = float(input("enter your third number : "))
fourth_number = float(input("enter your fourth number : "))

simple_compound_interest = input("""please choice the option
si for simple 
ci for compound interest
""")

if simple_compound_interest == "si":
   print(" si = ", (first_number * second_number * third_number/100))
else:
   print(" ci = ", (first_number * 1 + (third_number / fourth_number), ^ fourth_number * second_number,))
   print("invalid option")
