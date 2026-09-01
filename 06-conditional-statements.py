## Conditional Statements
'''
The most common conditional statements used for decision-making in programming are:

* `if`
* `if-else`
* `if-elif-else`

## Syntax

* If the condition is true, the code block under the if branch is executed, and the code block under the else branch is skipped.

* If the condition is false, the code block under the else branch is executed, and the code block under the if branch is skipped.

### if condition:

# code to be executed if the condition is true

### else:

# code to be executed if the condition is false

'''

#Example 

weather = input()

if weather == "sunny":
    print("play cricket")
    print("good")

print("code ended hear !!!!")


## if-else 

weather = input("Give current weather:")

if weather == "sunny":
    print("play cricket")

else:
    print("play robo game at home ")

print("code ended hear!!!")    

# if-elif-else

weather = input("enter weather:")

if weather == "sunny":
    print("play cricket")

elif weather == "rainy":
    print("play with robo")
else:
    print("going to sleep")
print("code ended hear !!!") 

'''
if condition1:
    # code to be executed if condition1 is true

elif condition2:
    # code to be executed if condition2 is true

elif condition3:
    # code to be executed if condition3 is true

else:
    # code to be executed if none of the conditions are true
'''        
   # Example :

weather = input("enter the weather:")
time_of_day = input("enter it's day or night:")

if weather == "sunny" and time_of_day == "day":
    print("you can play with car toy")

elif weather == "rainy":
    print("play with boat toy")

elif weather == "snowey" and time_of_day == "night":
    print("you can play with your teddy bear toy")

else:
    print("you can play with snowman toy")

print("Stay worm and have a grate day!!!") 

## Nested if Statements

weather = input("enter weather:")
time_of_day =("enter day or night:")

if weather == "sunny":
    if time_of_day == "day":
        print ("you paly with your car toy")
    else:
        print("its's night. time to sleep")
elif weather == "rainy":
    print("play with boat toy")
elif weather == "snowy":
    if time_of_day == "night":
        print("you play with teddy bear toy")
    else:
        print("you play with your snowman toy.")
else:
    print("you stay inside and read a story book")
print("code ended haer!!!")    


         