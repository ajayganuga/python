## Functions 
"""
Function

Functions are blocks of organised, reusable code that 
perform a specific task.

Dividing a complex problem into smaller chunks makes 
our program easy to understand and reuse.

Types :

FUNCTIONS

1. PRE DEFINED

   * Library functions

2. USER DEFINED

   * User defined functions, to reduce complexity of big programs


"""

## Declaration/Defining
'''
You define a function using the def keyword, followed by the 
function name, parentheses (), and a colon :.

Syntax

def function_name(parameters):
# Function body

'''

## Function Call
'''
To execute a function and run the code inside it, you 
call the function by using its name followed by parentheses ().

Syntax

function_name(arguments)
'''

## # Parameters and Arguments
'''
* **Parameters** are defined in the function's parentheses during the **function definition**.

* **Arguments** are the actual values passed to the function when it is **called**.

* Functions can take input values known as **parameters or arguments**.

'''

## Return Statement
'''
Functions can return a value using the return statement. 
The returned value can be assigned to a variable or used in expressions.

'''


def add(a,b):
    return a+b

result = add(3,5)
print(result)

## All at One Place

'''
def function_name(parameters):
    # statement
    return expression


* `def` → Keyword
* `function_name` → Function name
* `parameters` → Parameter
* `# statement` → Body of Statement
* `return expression` → Function return

'''

## Positional Arguments
'''
These are the most common type of arguments and are passed
 to a function based on their position. The order of the arguments in the
 function call must match the order of the parameters in the function definition.

 '''

def  add_numbers(a,b):
    return a+b
result=add_numbers(5,3)
print(result)


## Keyword Arguments
'''
You can pass arguments to a function using their names explicitly,
known as keyword arguments. This allows you to pass arguments in any order.

'''
def personal_info(name,age):
    print("Name:",name)
    print("Age:",age)

personal_info(age=24,name="Ajay")


## Default Arguments
'''
Default arguments are used to provide default values for parameters in 
case no value is passed during the function call. If no argument is provided for a default parameter, 
the default value will be used.
'''

def greet_user(name,greeting="Hello"):
    return greeting + "," + name + "!"

greeting1= greet_user("Bob")
greeting2= greet_user("Charlie","Hi")

print(greeting1)
print(greeting2)


