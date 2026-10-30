#Find the second largest number using python programming language 

numbers = [10, 25, 5, 40, 30]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest number
