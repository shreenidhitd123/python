#Armstrong Number Checker using python programming language 

num = int(input("Enter a number: "))

order = len(str(num))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** order
    temp //= 10

if num == total:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
