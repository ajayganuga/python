### Tuple 

'''
What is a Tuple?
================

A tuple is a collection of elements that is ordered and 
immutable (cannot be changed after creation).

# Example:
==========

T = (20, 'Jessa', 35.75, [30, 60, 90])

      20       'Jessa'       35.75       [30, 60, 90]
      ↑           ↑            ↑               ↑
     T[0]        T[1]         T[2]            T[3]

'''

##  # Definition
'''
* A tuple is an **ordered, immutable** collection of elements in Python.

* It is similar to a **list**, but the main **difference** is that tuples **cannot be changed** after creation.

* Once a tuple is created, you cannot **add, remove, or modify** its elements.

'''
## Creating Tuple
'''
To create a tuple, you use parentheses () with elements separated by commas.

my_tuple = ()

# Tuple with elements
my_tuple = (1, 2, 3)

Note: Tuples can also be created without parentheses, using comma-separated values.
====

'''

##  Accessing Values

'''
You can access the values in a tuple using square brackets `[]` with the index.

python
======
'''
my_tuple = (10, 20, 30)

print(my_tuple[0])  # Output: 10


## Methods
'''
Tuples have limited built-in methods due to their immutability.
Some common methods include `count()` and `index()`.

python
======

'''

my_tuple = (1, 2, 3, 2)

# Count the occurrences of a value in the tuple
count = my_tuple.count(2)
print(count)  # Output: 2

# Find the index of the first occurrence of a value
index = my_tuple.index(3)
print(index)  # Output: 2



