# Program 140: Sum of Digits using python programming language 

num = int(input("Enter a number: "))
total = 0

for digit in str(abs(num)):
    total += int(digit)

print("Sum of digits:", total)
