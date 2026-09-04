### Scope Of Variables

## 1: Global Scope
'''
Variables defined outside of any function or block have a global scope. 
They can be accessed from anywhere in the program, including inside functions.

'''
 # Example :

global_var = 10

def  my_function():
    print(global_var)

print(global_var)

## Local Scope
'''
Variables defined inside a function have a local scope. 
They are accessible only within the function where they are defined and not from outside the function.

'''

def my_function():
    local_var =5
    print(local_var) #Accessible (prints 5)

my_function()
# print(local_var)  # Not accessible (raises NameError)
