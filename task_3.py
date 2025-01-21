# Inventory Management with defaultdict: 
# Create an inventory tracker where each product is stored under its category.
#  Use defaultdict for auto-creating empty categories.

from collections import defaultdict

# Create a defaultdict with a default
# value of an empty list
inventory = defaultdict(list)

# Add elements to the defaultdict and print it   keyss --. value
inventory['fruits'].append('apple')
inventory['vegetables'].append('carrot')
print(inventory)

# No key error raised here and an empty list
# is printed
#print(inventory['juices'])