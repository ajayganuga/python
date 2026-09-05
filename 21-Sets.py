### Sets

"""

## What is a Set?

A **set** is an unordered collection of **unique elements** in Python.

python
======

my_set = {1, 2, 3, 4}


* Sets are written using **curly braces `{}`**.
* Sets **do not allow duplicate values**.
* Sets are **unordered**, so elements do not have a fixed position or index.
* Sets are **mutable**, meaning we can add or remove elements.
   
"""

## ## Creating Sets
'''
Create a set by enclosing elements within curly braces `{}`.
Alternatively, you can use the `set()` function.

python
======
'''
# Creating an empty set
empty_set = set()

# Creating a set with elements
fruits = {'apple', 'banana', 'cherry'}

# Creating a set from a list
numbers = set([1, 2, 3, 4, 5])

## Adding Elements
'''
The add() method is used to add a single element to a set.
'''
my_set = {1, 2}
my_set.add(3)

print(my_set)  # Output: {1, 2, 3}

## Removing Elements
'''
You can remove elements from a set using the remove() or discard() methods.
'''
my_set = {1, 2, 3}
my_set.remove(2)

print(my_set)  # Output: {1, 3}

## ## Set Operations
'''
*----> **Union**
*----> **Intersection**
*----> **Difference**
*----> **Symmetric Difference**

'''

## Set operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}


union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}


intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}


difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}


symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


## ## Set Membership and Length
'''
You can check if an element is present in a set using the `in` keyword. The `len()` function gives the number of elements in the set.

python
======
'''
my_set = {1, 2, 3}

print(2 in my_set)  # Output: True
print(4 in my_set)  # Output: False

print(len(my_set))  # Output: 3

## Frozen Sets
'''
A frozenset is an immutable version of a set.
'''
my_set = {1, 2, 3}

frozen_set = frozenset(my_set)


## Set Comprehensions
'''
Like lists and dictionaries, sets also support comprehensions for concise set creation.
'''
# Set comprehension to create a set of squares

squares = {x**2 for x in range(1, 6)}  # Output: {1, 4, 9, 16, 25}

## Set Methods
'''
Some common set methods include clear(), copy(), pop(), update(), and more.
'''

my_set = {1, 2, 3}

# clear()
my_set.clear()  # Removes all elements, resulting in an empty set

# copy()
new_set = my_set.copy()  # Creates a shallow copy of the set


# add()
my_set.add(4)  # Adds a single element

# remove()
my_set.remove(2)  # Removes the specified element

# discard()
my_set.discard(5)  # Removes an element without raising an error if it doesn't exist

# pop()
my_set.pop()  # Removes and returns an arbitrary element

# update()
my_set.update({4, 5})  # Adds multiple elements to the set