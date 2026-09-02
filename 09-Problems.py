## program 1 :

'''
Vowel Counter

Write a program that takes a string input from the user and
counts the number of vowels (A, E, I, O, U, and their lowercase
equivalents) in the string.

Sample Input:  "Hello, World!"

Sample Output: Number of vowels: 3
'''


s = input()
s = s.lower
a = s.count('a')
e = s.count('e')
i = s.count('i')
o = s.count('o')
u = s.count('u')
total = a+e+i+o+u
print(f"Number of vowels:{total}")


## Program :2

'''
Grade Calculator

Create a program that takes the marks of a student in different
subjects as input. Calculate the total marks and average, and
then display the corresponding grade based on the average.

Sample Input:
Marks in Math: 85
Marks in Science: 90
Marks in English: 78

Sample Output:
Total Marks: 253
Average Marks: 84.33
Grade: A

'''
m = int(input("Marks in Math:"))
s = int(input("Marks in Science:"))
e = int(input("Marks in English:"))
total = m+s+e
average = total/3

grade = ""

if average >=80:
    grade = "A"
elif average >=60:
    grade = "B"
else:
    grade = "p"

print(f"Total Marks:{total},\nAverage Marks:{average},\nGrade:{grade}")


## Program :3

'''
Palindrome Checker

Write a program that takes a string input from the user and
checks if it is a palindrome or not. A palindrome is a word,
phrase, number, or sequence of characters that reads the same
backward as forward.

Sample Input:  "radar"

Sample Output: It is a palindrome.

'''
data = input("enter any string:")
reverse = data[::-1]
if reverse == data:
    print("it is a palindrome.")
else:
    print("worng statement.")

## Program :4
'''
Largest of Three Numbers

Write a program that takes three numbers as input and finds
the largest among them using decision-making statements.

Sample Input:
Enter three numbers: 15, 8, 21

Sample Output:
The largest number is 21.

'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is", largest)
  
