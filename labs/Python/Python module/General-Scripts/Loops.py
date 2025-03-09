"""
Use a while loop
Use a for loop
"""

import random
number = random.randint(1,10)
print("PC guessed number:",number)


print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")


isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        

for x in range (0, 11):
    print(x)