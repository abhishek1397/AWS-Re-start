"""
Write Python code that uses the string data type
Concatenate strings
Use the string to get input
Format strings for output
"""

myString = "This is a string."
print(myString)
print("\n")

print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print("\n")


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print("\n")

name = input("What is your name? ")
print(name)
print("\n")


color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))


