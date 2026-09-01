## What are Strings?
'''
Strings are a data type used to represent textual data.

They are sequences of characters and are enclosed in either:

* **Single quotes** (`' '`)
* **Double quotes** (`" "`)
* **Triple quotes** (`''' '''` or `""" """`)
'''
# How to Create String?
'''
You can create strings using single,
double, or triple quotes. Triple quotes are used for multiline
strings or to include special characters like line breaks.

• single_quoted = 'Hello, world!'

• double_quoted = "Hello, world!"

• multiline = """Hello,

world!

Welcome"""`

'''
# String Indexing
'''
Strings are ordered sequences, 
and you can access individual characters 
using indexing. Python uses zero-based indexing, 
where the first character has an index of 0.

Example:

str = "PyTHON"

Positive index →  0   1   2   3   4   5
                  P   Y   T   H   O   N

Negative index → -6  -5  -4  -3  -2  -1
'''

# Example

str = "PYTHON"

print(str[0])
print(str[3])
print(str[5])
print(str[-2])

#######  String Slicing : Taking a small part of a string from a larger string.
'''
Name = "Michael Jackson"

string_variable[start:stop:step]

* start → Starting Index
* stop → Last/End Index
* step → Increment

'''
# Example

s = 'hello world'

print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1]) 
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])

## String Concatenation
'''
You can concatenate strings using the **+ operator**:

String 1 + String 2
'''

# Example

first_name= "Ganuga"
last_name = "Ajay"
full_name = first_name +" "+ last_name
print(full_name)

## # String Length
'''
You can find the length of a string using the len() function.

*Example:

len(string)


*Length = Number of characters in a string.
'''

# Example 1 :

string1 = "coding is fun!"
print(len(string1))

# # Example 2 :

string2 = "Hello, World!"
print(len(string2))

# # Example 3 :

string3 = ("abcdefghijklmnopqrstuvwxyz")
print(len(string3))

# # Example 4 :

string4 = "my name is ajay i am from beluguppa "
print(len(string4))

## String Methods
'''
Python provides numerous built-in methods 
for manipulating strings, such as converting cases, 
removing whitespaces, replacing characters, splitting, 
joining, and more.

'''
# examples
#python srting manipulation Examples:

# define the original string

s = "Hello, world!"

# 1 : Convert the string to uppercase.

print(s.upper())

# 2 : Converting the sting to lowercase.

print(s.lower())

# 3 : Remove leading and trailing whitespace from the string.

print(s.strip())

# 4: Replace all occurrences of 'o' with 'x' in the string.

print(s.replace('o','x'))

# 5: count the number of occurences of 'a' in the string.

print('abababaaadsaaa'.count('a'))

'''
String Methods

• str.upper()
• str.lower()
• str.capitalize()
• str.title()
• str.strip()
• str.lstrip()
• str.rstrip()
• str.startswith(prefix)
• str.endswith(suffix)
• str.replace(old, new)
• str.split(separator)
• str.join(iterable)
• str.find(substring)
• str.rfind(substring)
• str.index(substring)
• str.rindex(substring)
• str.count(substring)
• str.isalnum()
• str.isalpha()

'''

## String Formatting
'''
Python supports multiple ways of formatting strings,
including old-style % formatting, str.format(), and f-strings
(formatted string literals).

print ("My name is %s %s and my age is %d" % ("John", "Doe", 45))

'''
# Examples

name = "Alice"
age = 30

# Using the '%' operator for string formatting (old-style)
print("My name is %s and I am %d years old." % (name, age))

# Using the 'format()' method for string formatting
print("My name is {} and I am {} years old.".format(name, age))

# Using f-strings (formatted string literals) for string formatting
print(f"My name is {name} and I am {age} years old.")

## Escape sequences
'''
Special character combinations that are used to represent
characters that are otherwise difficult or impossible to include
directly in a string.

\ : Backslash
\' : Single Quote
\" : Double Quote
\n : Newline (line break)
\t : Tab
\r : Carriage Return (used for some text file formats)
\b : Backspace (moves the cursor back one space)
\f : Form Feed (used for some text file formats)
\v : Vertical Tab (rarely used)

'''

# Examples

print("Hello\"s world!")

print("Hello\'s world!")

print("Hello\ns world!")

print("Hello\bs world!")

print("Hello\fs world!")

print("Hello\rs world!")

print("Hello\ts world!")

print("Hello\\s world!")

print("Hello\vs world!")
