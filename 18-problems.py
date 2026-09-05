## 1: Finding the Sum of Two Numbers
'''
Sample Input:

num1 = 5
num2 = 10

Sample Output:

Sum: 15

Topics Covered:

Input and Output, Variables, Arithmetic Operators.
'''
a=int(input("num1 = "))
b=int(input("num2= "))

def add_2numbers(a,b):
    print(a+b)

add_2numbers(a,b)


## 2: Finding the Area of a Circle
'''
Sample Input:
radius = 5

Sample Output:
Area of the circle: 78.53981633974483

Topics Covered:
Input and Output, Variables, Arithmetic Operators.

'''

def area(r):
    circleArea = 3.14*(r**2)
    return circleArea
radius = 4
a = area(radius)

print(a)

## 3: Solving Quadratic Equations
'''
Sample Input:
a = 1
b = -3
c = 2

Sample Output:
Roots: (2.0, 1.0)

Topics Covered:
Input and Output, Variables, Arithmetic Operators.

'''

def calculateroots(a,b,c):
    root =0
    root =0
    d =(b**2)-4*a*c
    root1=(-b+(d**(0.5)))/2*a
    root2=(-b-(d**(0.5)))/2*a
    print(f"Roots:({root1},{root2})")

x=int(input("Give a: "))
y=int(input("Give b: "))
z=int(input("Give c: "))

calculateroots(x,y,z)

## 3: Swap the values of two variables without using a temporary variable
'''
Sample Input:
a = 10
b = 20

Sample Output:
After Swapping
a = 20
b = 10
'''
def swap(a,b):
    b=b+a
    a=b-a
    b=b-a
    print(f"value of a is: {a}")
    print(f"value of b is: {b}")

swap(10,30)
swap(40,50)
swap(100,200)
