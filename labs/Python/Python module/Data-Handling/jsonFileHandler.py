"""
Create a module
Open a file and load the JSON data it contains using the built-in JSON module of Python
Parse the JSON structure to access insulin data
Calculate the rough molecular weight of human insulin using given code (similar to the lab Working with the String Sequence and Numeric Weight of Insulin in Python)
"""


import json


def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data