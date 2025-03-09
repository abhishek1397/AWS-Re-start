"""
Add comments that explain the intention and flow of your code
Use print() to print elements of your Python code to the console
Use string manipulations to get the sequence of insulin from preproinsulin
Do basic math on the molecular weight and sequence of insulin
Assign string, int, and float variables to numbers that represent the weight of insulin
Explore Python exceptions

"""

# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:",preproInsulin)

# Store the remaining sequence elements of human insulin in variables:
lsInsulin= "malwmrllpllallalwgpdpaaa"
bInsulin=  "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin= "giveqcctsicslyqlenycn"
cInsulin= "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

insulin = bInsulin + aInsulin
print(insulin)