empty_list = []

empty_list.append("apple")
empty_list.append("banana")

print(empty_list)

empty_list.remove("banana")
print(empty_list)

empty_list.append("apple")#add list
empty_list.append("banana")
empty_list.append("apple")#add list
empty_list.append("banana")

for index, fruit in enumerate(empty_list):
    print(f"item position: {index} and value: {fruit}")# for loop syntax
    #tuple

x = ("apple", "banana")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(tuple(y))

fruits = ("apple", "banana", "cherry", "orange", "rasberry")

print(fruits[1])
(green, yellow, *red) = fruits

print(green, yellow, red)

fruits = ("apple", "banana", "cherry", "orange", "rasberry")

print(fruits[1])
(green, *yellow, red) = fruits

print(green, yellow, red)
fruits = ("apple", "banana", "cherry", "orange", "rasberry")

print(fruits[1])
(*green, yellow, red) = fruits

print(green, yellow, red)
fruits = ("apple", "banana", "cherry", "orange", "rasberry")

print(fruits[1])
(green, yellow, *red) = fruits

print(green, yellow, red)
#for set
fruits = { "banana", "cherry", "orange", "rasberry"}

for item in fruits:
    print(item)

fruits.add("apple")
print(fruits)

