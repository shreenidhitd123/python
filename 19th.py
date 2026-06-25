# Armstrong Number Check using python programming language 

num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
