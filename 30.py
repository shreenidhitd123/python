#Palindrome Checker using python programming language 

text = input("Enter a word: ")

if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
