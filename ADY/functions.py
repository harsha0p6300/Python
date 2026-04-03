# def fahrenheit_to_celsius(f):
#     c=("Vardhan")
#     print(c)
# fahrenheit_to_celsius("harsha",c)
# fahrenheit_to_celsius(95)
# fahrenheit_to_celsius(50)
# age="20"
# print("my age"+str(age))

# def add(a,b):
#     c= a+b
#     print(c)

# add(5,9)
#using the fucntions
def show_man(age):
    print(f"the age is {age}")
show_man(29)

#using the lamda functions
add=lambda a,b:a+b
print(add(4,9))

#Add 10 to aurgument a, and return the result:
x=lambda a:a+10
print(x(10))

#multiply arguments a with argument b and result the result
x=lambda a,b:a*b
print(x(3,4))

#square of a number using lambda function
square=lambda a:a*a
print(square(5))

#Takes a string and returns it in uppercase
upper=lambda a:a.upper()
print(upper("harsha"))

#nums = [1, 2, 3, 4, 5], use map() and a lambda function to create a new list where each number is multiplied by 10
nums = [1, 2, 3, 4, 5]
a=lambda mul:mul+5
x=map(a,nums)
print(list(x))

#Make new fruits by sending two iterable objects into the functions

fruits=["Apple,Mango,Banana"]
colours=["Red,white,Yellow"]


