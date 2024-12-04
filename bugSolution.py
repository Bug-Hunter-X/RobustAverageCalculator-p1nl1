def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case gracefully
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 0

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}") #Output: Average: 3.0