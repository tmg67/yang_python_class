def natural_numbers():
    n =1 
    while True:
        yield n 
        n += 1
#example usage:
gen = natural_numbers()
for _ in range(10): #print the first 10 numbers
    print(next(gen))

treasures = ["gold", "silver", "gem", "gold"]
upper_treasure = []
for treasure in treasures:
    upper_treasure.append(treasure.upper())
#task 1 : use a list comphrehension to capitalize all treasures.
capitalized_treasures = [treasure.upper() for treasure in treasures]
print(capitalized_treasures)

def factorial(n):
    if n == 0:
        return 1 #base case
    return n *factorial(n-1)
print(factorial(5))