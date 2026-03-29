# Example: Squaring numbers in a list using map() with a custom function
def square(x):
  return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers_map = map(square, numbers)

# map() returns an iterator, so we convert it to a list to see the results
print(f"Original numbers: {numbers}")
print(f"Squared numbers (using map with function): {list(squared_numbers_map)}")

# Example: Squaring numbers using map() with a lambda function
squared_numbers_lambda = map(lambda x: x * x, numbers)
print(f"Squared numbers (using map with lambda): {list(squared_numbers_lambda)}")

# Example: Adding two lists element-wise using map() with a lambda function
list1 = [10, 20, 30]
list2 = [1, 2, 3]

sum_lists = map(lambda x, y: x + y, list1, list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Sum of lists (element-wise): {list(sum_lists)}")