# problem : 1
'''
Print numbers from 1 to N

Take a positive integer N as input and print all the numbers from 1 to N.

Sample Input:

N = 5

Sample Output:

1
2
3
4
5

'''

n= int(input("N:"))
i =1
while i <=n:
    print(i)
    i +=1 # i = i+1

## Problem : 2

'''
Calculate the sum of N natural numbers

Take a positive integer N as input and calculate the sum of the first N natural numbers.

Sample Input:

N = 5

Sample Output:

Sum of first 5 natural numbers: 15

'''

n = int(input("enter value of N:"))

i = 1
sum =0
while i<=n:
    sum=i+sum
    i+=1
print(sum)  

## Problem : 3

'''
Print even numbers from 1 to N

Take a positive integer N as input and print all the even numbers from 1 to N.

Sample Input:

N = 10

Sample Output:

2
4
6
8
10

'''

n = int(input("Enter value of N :"))

i = 1

while i <=n:
   if   i % 2==0:
    print(i)
   i += 1

## Problem : 4

'''
Multiplication table of a number

Take a positive integer N as input and print the multiplication table of N from 1 to 10.

Sample Input:

N = 3

Sample Output:

Multiplication table of 3:

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
'''

n = int(input("enter value of N: "))

i = 1

while i<=10:
    print(f"{n} x {i} ={n*i}")
    i+=1

## using for loop 

n = int(input("enter value of N: "))
i = 1

for i in range(1,11):
     print(f"{n} x {i} ={n*i}")
    

## problem : 5

'''
Calculate the factorial of a number

Take a positive integer N as input and calculate its factorial (N!).

Sample Input:

N = 5

Sample Output:

Factorial of 5: 120

'''

n = int(input("Give n value:"))
fact = 1

while n>0:
    fact =fact*n
    n-=1
print(fact)
