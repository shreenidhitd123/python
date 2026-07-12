#Find the Largest Number in a List using python programming language 

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = max(numbers)

print("Largest number:", largest)
