#example 5: exception
#Example 5 : handling division by zero
try:
    result = 10/0
except ZeroDivisionError as e:
    print("exception:", e)#output: exception: division by zero

#Example5.2: handling index out of range
try:
    my_list = [1,2,3]
    print(my_list[5])
except IndexError as e:
    print("exception:", e) # output: exception:list index out of range 

class NoMoneyException(Exception):
    pass
class OutofBudget(Exception):
    pass
balance = int(input("enter a balance to withdraw:"))
try:
    if balance < 1000:
        raise NoMoneyException("you have  no money to withdrawn")
    elif balance > 10000:
        raise OutofBudget("you have reached your limit")
except Exception as error:
    print((error))