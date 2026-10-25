# Python program to find the second largest number

numbers = [10, 25, 45, 30, 50, 20]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second largest number:", unique_numbers[-2])
