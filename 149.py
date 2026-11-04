# Program to check palindrome string using python programming language 

text = input("Enter a string: ")

if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
