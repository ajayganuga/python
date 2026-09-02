## Leap Year Checker
'''
Write a program that takes a year as input 
and checks if it is a leap year or not.

Hint: A leap year is divisible by 4, except for years that
are divisible by 100 but not divisible by 400.

Sample Input:
Enter a year: 2024

Sample Output:
It is a leap year.

'''
year = int(input("Enter any year:"))

if year%100 == 0 and year%400 != 0:
    leap = False
elif year%4 == 0:
    leap = True
else:
    leap = False
print(leap)
