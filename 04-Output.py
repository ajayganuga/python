# ## Output
# '''
# Defination
# ----------

# --> The print() function is used to display output to the console or terminal. it allows you to show information

# --> *objects
# --> sep
# --> end
# --> file
# --> flush

# '''
# # 1.*objects

data = (20,30,40,50,60,)
print (*data)

# # 2. separate

a = int(input("give a number:"))
b = int (input("give b number"))

# print(a,b,sep=" differrent ")

# # 3. end 

a = int(input("give a number:"))
b = int (input("give b number"))

print(a,b,sep=" , ",end=" Ended here.")

# # Example 1 : String input and Output
# """
# Expected input : "John"

# Expected output : "Hello,John!"

# """
name = input("enter name:")
print ("Hello",name,sep=", ",end="!")

# Example 2 : Integer input & output

"""
Expected input : 5

Expected output : "you entered: 5"

"""
a = int(input("Enter a number :"))
print ("You entered:",a)

# Example 3: Float input and output
'''
Expected input : 3.14

Expected output : "Value of Pi:3.14"

'''
a = float(input("enter value of a:"))
print ("Value of Pi:",a,sep="")

# Example 4 : taking Multiple inputs in a single line
'''
Expected input : 10 20 30

Expected output: "sum of inputs:60"

'''
a = (input("enter value of a:"))
x,y,z =a.split(" ")
sum = int(x)+int(y)+int(z)
print("Sum of Inputs:",sum,sep="")

# Example 5 : Specifying Separator in Output
'''
Expected input : "John",25

Expected output: "Name:John,Age:25"
'''
data = input("enter name and age:")
x,y= data.split(",")
print ("Name:",x,",Age:",y,sep="")

# Example 6: End parameter in Output
'''
Expected input : 5

Expected output: "Countdown:5 4 3 2 1 Blast off!"
'''
a = input("enter a number:")
print ("Countdown:",a,"4 3 2 1 ",end="Blast Off!")

# Example 7: Arithmetic Operators
'''
Expected input : 10,5

Expected output:
"Addition:15,Subtraction:5,
Multiplication:50,Division:2.0"

'''

x,y= input("enter a and b values:").split(",")
a= int(x)
b= int(y)

print ("Addition:",a+b,",Subtraction:",a-b,
",Multiplication:",a*b,",Division",a/b,sep="")

# Example 8 : Comparison Operators
'''
Expected input : 10,5

Expected output:
"10>5:True,10<5:false,
10==5:False,10!=5:True"
'''
x,y = input("Enter x and y values:").split(",")
a= int(x)
b= int(y)
print("10>5:",a>b,",10<5:",a<b,",10==5:",a==b,",10!=5:",a!=b,sep="")

# Example 9 
'''
Expected input : True,False

Expected output:
"True and False:False,
True or false:True,not True:False"

'''
x,y=input("enter conditions:").split(",")
a= bool(x)
b= bool(y)
print("True and False:",a and b,",True or False:",a or b,",not True:",not a,sep="")

# example 10: Taking Yes / No Input and Handling case Sensitivity
'''
Expected input : Yes(or yes,YES,yEs,etc.)

Expected output: " you entered:Yes"

'''
# data = input("Enter yes in multiple ways: ").split()[0].capitalize()

# print("You entered:", data)

# Example 11: Formatting Output using f-strings
'''
Expected input : "Alice",25

Expected output:"Name:Alice,Age:25 years"
'''
x,y = input("Enter name ,Age:").split(",")

print("Name:",x,",Age:",y,end="years",sep="")

#Method 2 
x,y = input("Enter name ,Age:").split(",")

print(f"Name:{x},Age:{y}years")