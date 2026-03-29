#Lambda with Built-in Functions
#Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
#Actually map() and lambda are not the same thing — they do different jobs, but they often work together.

#Difference between map() and lambda
#Lambda = small function

#A lambda is a short anonymous function.

#It tells what operation to perform.

x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

# Write a lambda function that takes a string and returns it in uppercase.
name=lambda text:text.upper()
print(name('harsha'))

#  Write a lambda function that takes an integer and returns "Even" if it's even, and "Odd" if it's odd.
num=lambda z:"even"if z%2==0 else "odd"
print(num(5))

# Given a list of numbers [1, 2, 3, 4, 5], use map() and a lambda function to create a new list containing the squares of these numbers.

num=[1,2,3,4,5]

square=map(lambda z:z*z,num)
print(list(square))


#  Given a list of dictionaries representing people (e.g., [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]), use map() and a lambda function to extract just a list of their names.

dict=[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
name=list(map(lambda people:people["name"],dict))
print(name)

