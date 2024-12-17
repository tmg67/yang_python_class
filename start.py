print("hello world")

if 5 > 2: #if variable = garna payana
    print("5 is greater")
    print("2 is smaller")

    x = 5
    y = "hello world"
    print(id(x))
    print(id(y))# gives memory id of variable
    print(type(x))
    print(type(y))# type check
    # its skips
    mail = """
    multi
     line string"""
    print("mail")
    age = 8
    Age = 4# they are different vairiable
 
    myObject = 5 #camel case
    MyObject = 5 # pascal case(class )
    my_object = 5 # snake case ( fucntion and variable case use)

    x,y,z = "orange", "banana", "apple" 
    print(x, y, z)

    fruits = ["orange", "banana", "apple"]
    x, y, z = fruits
    print(x, y, z)

    a = True
    b = False
    print( a and b)
    print( a or b)
    print(not b)

    boy_age = 19
    boy_country = "Nepal"

    if boy_age > 18 and boy_country == "Nepal":
          print("boy can give licence exam in Nepal") 

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

    print("division = ", first_number / second_number)