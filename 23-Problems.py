## Problem : 1
'''
Find the sum of all elements in a given list of numbers.

Sample Input: [10, 20, 30, 40, 50]

Sample Output: Sum of elements = 150

'''

list = [10,20,30,40,50]
sum =0
for i in list:
    sum += i
print(f"sum of elements = {sum}")


##  Find the maximum and minimum values in a list of numbers.
'''
Sample Input: 15, 2, 7, 25, 10

Sample Output: Maximum = 25, Minimum = 2

'''

# User input separated by commas
numbers = [int(x) for x in input("Enter numbers: ").split(",")]

maximum = max(numbers)
minimum = min(numbers)

print(f"Maximum = {maximum}, Minimum = {minimum}")

## Remove duplicate elements from a list to create a new list with unique element
'''
Sample Input: [10, 20, 30, 20, 40, 10, 50]

Sample Output: [10, 20, 30, 40, 50]

'''

numbers = [10, 20, 30, 20, 40, 10, 50]

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)
# Output: [10, 20, 30, 40, 50]

## Count the number of occurrences of a specific element in a list.
'''
Sample Input:[1, 2, 3, 2, 1, 4, 2, 5]
            2

Sample Output:

Count of 2 = 3

'''

numbers = [1, 2, 3, 2, 1, 4, 2, 5]
target = 2

count = 0
for num in numbers:
    if num == target:
        count += 1

print(f"Count of {target} = {count}")