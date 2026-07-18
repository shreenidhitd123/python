#Number Guessing Game using python programming language 

import random

number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("Congratulations! You guessed it correctly.")
else:
    print("Wrong guess!")
    print("The correct number was:", number)
