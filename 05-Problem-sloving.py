# problem solving
## 1 . Find the sum of two numbwrs 
'''
sample input : num1 = 5
               num2 = 10

sample Output : Sum:15

Topics covered :
Input and Output, Variable, Arithmetic Operators.

'''
num1 = int(input("Enter value of num 1:"))
num2 = int(input("Enter value of num 2:"))

print("sum:",num1+num2,sep="")
print(f"sum:{num1+num2}")

## 2 Finding the Area of a Circle
'''
Sample Input:      radius = 5


Sample Output:     Area of the circle: 78.53981633974483


Topics Covered:

Input and Output, Variables, Arithmetic
Operators.

'''
radius = int(input("enter the value :"))
value = 3.14*radius*radius
data = 3.14*(radius**2)
print("Area of the circle:",value)
print("Area of the circle:",data)
print("Area of the circle:",3.14*radius*radius)

## 3.  (roots .py) Solving Quadratic Equations
'''
Sample Input:

a = 1
b = -3
c = 2


Sample Output:

Roots: (2.0, 1.0)


Topics Covered:

Input and Output, Variables, Arithmetic
Operators.
'''
a= int(input("Give a: "))
b= int(input("Give b: "))
c= int(input("Give c: "))

d = (b**2)-4*a*c
root1 = (-b +(d**(0.5)))/2*a
root2 = (-b -(d**(0.5)))/2*a

print(f"Roots:({root1},{root2})")

## 4. Swap the values of two variables
'''
without using a temporary variable


Sample Input:

a = 10
b = 20


Sample Output:

After Swapping

a = 20
b = 10

'''
# with using temp

a= int(input("enter value of a:"))
b= int(input("enter value of b:"))
temp = a
a=b
b=temp
print("After Swapping")
print("a=",a,sep="")
print("b=",temp,sep="")

# without using temp

a= int(input("enter value of a:"))
b= int(input("enter value of b:"))
a=a+b
b=a-b
a=a-b
print("After Swapping")
print("a=",a,sep="")
print("b=",b,sep="")

## 5. Converting Temperature Units

'''
Sample Input:

temperature_celsius = 30


Sample Output:

Temperature in Fahrenheit: 86.0
Temperature in Kelvin: 303.15


Topics Covered:

Input and Output, Variables, Arithmetic
Operators.

'''
c = int(input("temperature_celsius ="))
f = c*(9/5)+32
k = 273.15+c
print(f"Temperature in Fahrenheit:{f}")
print(f"Temperature in Kelvin:{k}")

## 6 . Basic Currency Converter

'''
Sample Input:

amount_in_usd = 100
exchange_rate_usd_to_eur = 0.85


Sample Output:

Equivalent amount in EUR: 85.0

'''
a= int(input("amount_in_usd ="))
b= float(input("exchange_rate_usd_to_eur ="))
c = b*a
print(f"Equivalent amount in EUR:{c}")