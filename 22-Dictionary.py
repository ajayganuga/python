### Dictionary

# Defination
'''
A dictionary is an unordered collection of key-value pairs. 
Are used to store data in the form of key-value pairs, where each key is unique.

key : value_1

'''
## Creating Dictionaries
'''
To create a dictionary, you use curly braces {} and specify key-value pairs separated by colons :. Keys and values can be of any data type.
'''

# Creating a dictionary with name, age, and house information
my_dict = {'name': 'Harry', 'age': 11, 'house': 'Gryffindor'}

# Printing the dictionary
print(my_dict)

## Accessing Values
'''
You can access the values in a dictionary using square brackets [] with the key.
'''

my_dict = {'name': 'Harry', 'age': 11, 'house': 'Gryffindor'}

# Accessing the values in the dictionary
name_value = my_dict['name']
age_value = my_dict['age']
house_value = my_dict['house']

## Adding Values
'''
To add new key-value pairs or update existing ones in a dictionary, you can use square 
 brackets [] and the assignment operator =.
'''

my_dict = {'name': 'Harry', 'age': 11, 'house': 'Gryffindor'}

# Adding a new key-value pair to the dictionary
my_dict['gender'] = 'Male'

## Modifying Values
'''
You can change the value associated with a key in a dictionary.
'''

my_dict = {'name': 'Harry', 'age': 11, 'house': 'Gryffindor'}

# Modifying the 'age' value in the dictionary
my_dict['age'] = 12

###  **Methods**
"""
Dictionaries have several useful methods,

* keys()
* values()
* items()
* get()
* pop()
* update()

"""

## Looping
'''
You can use loops to iterate through the keys or values of a dictionary

'''

for key in my_dict:
    print(key)

# Loop through values
for value in my_dict.values():
    print(value)

# Loop through key-value pairs
for key, value in my_dict.items():
    print(key, value)


##  Comprehensions
'''
Similar to lists, dictionaries also support comprehensions for concise dictionary creation

'''

squares_dict = {x: x**2 for x in range(1, 6)}

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}    