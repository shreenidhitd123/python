# Python program to find the second largest number using python programming language 

numbers = [10, 25, 15, 40, 30]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second largest number:", unique_numbers[-2])
