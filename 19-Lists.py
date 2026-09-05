### Lists :
"""
Definition

• A list is a versatile and mutable data structure used to store 
  a collection of items.
• Defined using square brackets []
• Contain elements of different data types
• Allow duplicates.

"""

## Creating Lists
"""
You enclose the elements inside square brackets, separated by commas.

python
======
"""
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]



## Accessing Elements
"""
You can access individual elements of a list using their index. 
Indexing in Python starts from 0.

python
======
"""
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: "apple"
print(fruits[1])  # Output: "banana"

"""
Python also supports negative indexing, 
where -1 refers to the last element.
"""


##  # Slicing Lists
'''
You can extract a portion of a list using slicing. 
Slicing allows you to create a new list with a subset of elements.

python
======
'''
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])  # Output: [2, 3, 4]


## Modifying Elements
'''
You can modify individual elements in a list by accessing 
them using their index and then assigning a new value.
'''
# Example 

fruits = ["apple","banana","cherry"]
fruits[0] ="oreange"
print(fruits)  # Output:["orange","banana","cherry"]


## # Python List Methods
'''
append()
clear()

insert()
index()

remove()
count()

pop()
sort()

reverse()

'''
"""
append(): Adds an element to the end of the list.

insert(): Inserts an element at a specific index.

remove(): Removes the first occurrence of a specified element.

pop(): Removes and returns the element at a specified index (or the last element if no index is given).

index(): Returns the index of the first occurrence of a specified element.

count(): Returns the number of occurrences of a specified element in the list.

sort(): Sorts the list in ascending order.

reverse(): Reverses the order of the elements in the list.

"""

### Examples for all 

# 1. append()

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
# Output: [1, 2, 3, 4]

# 2. insert()

numbers = [1, 2, 4]

numbers.insert(2, 3)

print(numbers)
# Output: [1, 2, 3, 4]

# 3. remove()

numbers = [1, 2, 3, 2, 4]

numbers.remove(2)

print(numbers)
# Output: [1, 3, 2, 4]

# 4. pop()

numbers = [10, 20, 30, 40]

removed = numbers.pop(2)

print(removed)
# Output: 30

print(numbers)
# Output: [10, 20, 40]

# 5. index()

numbers = [10, 20, 30, 40]

position = numbers.index(30)

print(position)
# Output: 2

# 6. count()

numbers = [1, 2, 2, 3, 2, 4]

result = numbers.count(2)

print(result)
# Output: 3

# 7. sort()

numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)
# Output: [1, 2, 3, 5, 8]

# 8. reverse()

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)
# Output: [5, 4, 3, 2, 1]

### All methods together

numbers = [5, 2, 3, 2, 4]

numbers.append(6)
print(numbers)

numbers.insert(1, 10)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(3))

print(numbers.count(2))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

## List Concatenation
"""
Lists can be concatenated using the + operator, which creates 
a new list containing elements from both lists.
"""
# Example 

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

## List Comprehensions
"""
List comprehensions provide a concise way to create lists 
using a single line of code.

Syntax

new_list = [expression for item in iterable if condition]

"""
# Example 

squares = [i**2 for i in range(1,10)]
print(squares) # Output : [1, 4, 9, 16, 25, 36, 49, 64, 81]
