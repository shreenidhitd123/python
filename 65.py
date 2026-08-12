# Program to count vowels in a string using python programming language 

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
