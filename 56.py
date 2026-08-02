# Program to find the largest number in a list using python programming language 

numbers = [10, 25, 7, 45, 18, 32]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Numbers:", numbers)
print("Largest number:", largest)
