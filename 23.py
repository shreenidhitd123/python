# Armstrong Number Checker using python programming language 

num = int(input("Enter a number: "))

power = len(str(num))
total = sum(int(digit) ** power for digit in str(num))

if num == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
