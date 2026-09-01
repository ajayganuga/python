## Simple Calculator Program (Project)
'''
* Create a basic calculator program that performs addition, subtraction, multiplication, and division.
* Ask the user to enter two numbers and choose an operation.
* Display the result accordingly.
* Handle potential errors gracefully.
'''
num1 = int(input("enter one number:"))
num2 = int(input("enter one number:"))
operator = input("enter the operator: ")

if operator == "+":
    print(f"addition of two numbers is{num1+num2}")
elif operator == "-":
    print(f"subtractin of two numbers is{num1-num2}")
elif operator == "*":
    print(f"multiplication of two numbers{num1*num2}")
elif operator == "/":
    print(f"division of two numbers{num1/num2}")
else:
    print("not valid")
print("code ended hear!!")
