# Program 127: Sum of Digits

num = int(input("Enter a number: "))
total = 0

for digit in str(abs(num)):
    total += int(digit)

print("Sum of digits:", total)