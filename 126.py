# Program 126: Count vowels in a string using python programming language 

text = input("Enter a string: ")
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
