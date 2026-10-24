# Program to count vowels and consonants using python programming language 

text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", conson
