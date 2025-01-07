num1=input("enter first number")
num2=input("enter second number")
num3=input("enter third number")
if num1>=num2 and num1>=num3:
    print(f"{num1} is the largest number")
elif num2>=num1 and num2>num3:
    print(f"{num2} is the largest number")
elif num3>=num1 and num3>=num2:
    print(f"{num3} is the largest number")