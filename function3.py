number_list = [1, 2, 3, 4, 5]
def sum(*args):
 result(0)
for number in args:
   result += number
     return result

def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def exponential():
    pass
def print_name (name="yangji"):
    print(f"hello {name}")

    print(sum(1, 2, 3, 4, 5))
    print_name()
    print_name("yangji") 

def print_full_name(**kwargs):
    print(kwargs)
    print(f"my full name is{kwargs["first_name"]} {kwargs["last_name"]}")

    print_full_name(first_name="ruman", last_name="dangol", middle_name="none")
































































































































    
