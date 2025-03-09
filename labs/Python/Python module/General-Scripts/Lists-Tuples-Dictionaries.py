"""
Use the list data type
Use the tuple data type
Use the dictionary data type___
"""


myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print("\n")

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
print("\n")


myFruitList[2] = "orange"
print("Updated fruit list:{}!".format(myFruitList))
print("\n")


myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print("\n")

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print("\n")

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print("\n")

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
print("\n")

print(myFavoriteFruitDictionary.keys())

