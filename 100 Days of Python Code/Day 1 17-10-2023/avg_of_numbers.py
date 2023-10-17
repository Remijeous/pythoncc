user_input = input("Enter a list of numbers separated by commas: ")
numbers = user_input.split(',')
numbers = [int(number) for number in numbers]
average = sum(numbers) / len(numbers)
print("Average of number in the list is: ", average)