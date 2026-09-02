## Loops
'''
Loops are used to execute a block of code 
repeatedly as long as a certain condition is 
true or for a specific number of iterations.

Types

• while
• for

'''

## while loop
'''
The while loop executes a block of code as 
long as a specified condition is true. 
It continuously checks the condition before each 
iteration and stops when the condition becomes false.

Syntax:

while condition:
# Code block to be executed repeatedly

'''
# Example to while loop :

candies = 10

while candies > 0:
    # Give one candi to a friend
    print("Give a candy to a friend!")
    # Decrese the number of candies
    candies -= 1

## for loop:
'''
A for loop is a way to repeat a block of code for
 each item in a collection (like a list) or for a specific range of numbers.

Syntax:

for variable in range(start, stop, step):
# Code block to be executed for each variable

'''

# Example to for loop

candies = 10

# Using a for loop to give candies to a friens
for i in range(candies):
    # Give one candy to a friend 
    print("Give a candy to a friend!")

##  for loop for Sequence
'''
The for loop is used to iterate over a sequence (such as a list, tuple, string, or dictionary) and execute a block of code for each item in the sequence.

Syntax:

for item in sequence:
# Code block to be executed for each item

'''

# Example to for loop for sequence

message = "Hello, World"

for i in message:
    print(i)

# Example 2:

message = "Hello, World"
length = len(message)
for i in range( length ):
    print(i)

## Nested loops
'''
Nested loops refer to the situation where one loop is
 placed inside another loop. This allows you to execute 
 a set of instructions repeatedly.

Syntax:

for outer_var in outer_sequence:
# Code block of the outer loop
for inner_var in inner_sequence:
# Code block of the inner loop

'''
# Example for Nested Loop

# : Nested loop to generate a multiplication table from 1 to 5

for i in range(1,6):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")

## Break
'''
If during the execution of the loop Python interpreter encounters break, it immediately stops the loop execution and exits out of it.

Syntax:

while condition:
# Code block inside the loop
if some_condition:
break  # Exit the loop if the condition is met

'''

#Example 

candies = 10

# Using a for loop to give candies to a friend
for i in range(candies):
    # Give one candy to a friend
    print ("Give a candy to a friend!")

    # cheack if there are only 5 candies leaf
    if candies -i ==5:
        print("only 5 candies left. Stop distribution")
        break

## Continue
'''
Continue statement is used to skip the rest of 
the current iteration in a loop and move to the next 
iteration immediately.

Syntax:

while condition:  # Code block inside the loop
if some_condition:
continue  # skip this iteration

'''
# Example
candies = 10

# Using a for loop to give candies to a friend
for i in range(candies):
    # Check if there are only 5 candies left
    if candies -i == 5:
        print("only 5 candies left. Skipping this turn.")
        continue

    # Give one candy to a friend
    print("Giving a candy to a friend!")