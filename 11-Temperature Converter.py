## Temperature Converter:
'''
Build a temperature converter program that allows 
the user to convert temperatures between Celsius, 
Kelvin and Fahrenheit.

Sample Input:

Enter temperature: 32
Enter Units(K or F or C): C

Sample Output:

Temperature in Fahrenheit: 89.6F
Temperature in Kelvin: 305K

'''

t = int(input("Enter temperature: "))

a = input("Enter Units(K or F or C): ").upper()

f = t * (9/5) + 32
k = 273.15 + t

if a == "C":
    print("Temperature in Fahrenheit:", f, "F")
    print("Temperature in Kelvin:", k, "K")

elif a == "F":
    c = (t - 32) * (5/9)
    k = c + 273.15

    print("Temperature in Celsius:", c, "C")
    print("Temperature in Kelvin:", k, "K")

elif a == "K":
    c = t - 273.15
    f = c * (9/5) + 32

    print("Temperature in Celsius:", c, "C")
    print("Temperature in Fahrenheit:", f, "F")

else:
    print("Invalid Unit")        