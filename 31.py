#Number Guessing Game using python programming language 

import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("🎉 Congratulations! You guessed the correct number.")
else:
    print(f"❌ Wrong guess! The correct number was {secret_number}.")
