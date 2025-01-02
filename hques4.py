my_dict = {
    'name': 'John', 
    'age': 25,
    'city': 'New York'
}
my_dict['job'] = 'engineer'
my_dict['age'] = 26
my_dict.pop('city')
keys = my_dict.keys()
print(keys)
values = my_dict.values()
print(values)
print(my_dict)