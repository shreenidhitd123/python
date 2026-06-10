# Program to check whether a string is a palindrome using python programming language 
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
