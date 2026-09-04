### Lambda
"""
###  Lambda Function
     ===============

Definition:
A lambda function is a small, one-line function that can have any number
of arguments but can only have one expression.


Syntax:
------

lambda arguments: expression
============================


+----------+    +-----------+    +---+    +------------+
|  lambda  |    | arguments |    | : |    | expression |
+----------+    +-----------+    +---+    +------------+
      ↑                ↑             ↑            ↑
      |                |             |            |
   Keyword       Any number      Separates    Single
   to define     of arguments    arguments    expression
   function      can be passed   from         to evaluate
                                 expression

"""
#Examples:

# 1: Addition of Two Numbers:

add = lambda x, y: x + y

result = add(3, 5)

print(result)  # Output: 8

# 2: Squaring a Number:

square = lambda x: x ** 2

result = square(4)

print(result)  # Output: 16

