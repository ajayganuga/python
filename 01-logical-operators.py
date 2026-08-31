### Logical Operators
# (True == 1) , (False==0)
# 1.and Logical AND: Returns True if both conditions are True.

x = True
y = False

result_and = x and y
print ("Result of x AND y :", result_and)

# 2.or Logical OR: Returns True if at least conditions is True.

x = True
y = False

result_or = x or y
print ("Result of x or y :", result_or)

# 3.not Logical NOT: Returns True if the condition is False, and vice versa.

y = True

result_not= not y
print ("Result of not x :", result_not)

### Membership Operator 

#list of fruits
fruits =['apple','guva','banana','orange','grapes']

# 1. in Membership: returns True if the value is present inthe sequence.
# check if 'apple' in the list  

is_apple_in_list = 'apple'in fruits
print("'apple' is in the list:",is_apple_in_list)

# example 2

is_papaya_in_list = 'papaya'in fruits
print("'papaya' is in the list:",is_papaya_in_list)

# 2. not in Negated membership : Returns True if the value is not Present in the sequence.

# cheack if 'watermelon' is not in the list

is_watermelon_not_in_list = 'watermelon'not in fruits
print("'watermelon' is not in the list:",is_watermelon_not_in_list)

# example 2
is_apple_not_in_list = 'apple'not in fruits
print("'apple' is not in the list:",is_apple_not_in_list)

## identity Operators 

# 1. is identity: Returns True if both variables point to the same object
# 2. is not negated identity : Returns true if he variable piont to different object.

# Examples  

# Variables with the same value 
name1 ="john"
name2 ="john"

# check if name 1 and name 2 refer to different object i memory

result_is_not = name1 is not name2
print ("name1 is not name2?",result_is_not)


# variables with different values 

num1 = 10
num2 = 20 

# cheack if num1 and num2 refer to different objects in memory

resutl_is = num1 is not  num2
print("num1 is not num2?",resutl_is)

## Berwise Operators

# 1. Bitwise left shift(<<): Shifts the bits to the left by a specified number of positions

# 2. BItwise right shif(>>): Shifts the bits to the right by a specified number of positions  

# 1------->
result_left_shift = 2 << 2
print ("Bitwise Left Shift:",result_left_shift)

# 2-------->

result_right_shift = 32 >> 2
print ("Bitwise Right Shift:",result_right_shift)
