#In short
#A function is a block of code which only runs when it is called.

#A function can return data as a result.

#A function helps avoid code repetition.
def greet(name):

  print(f"Hello, {name}!")
  return

greet("Harsha")
#Return Values
#Functions can send data back to the code that called them using the return statement.

#When a function reaches a return statement, it stops executing and sends the result back:


def get_greeting():
  return "Hello world!"

message = get_greeting()
print(message)


student = "Ravi"
print("Hello " + student)


age = 20
print("Age is " + str(age)) #str(age) converts number to string.

def show_age(age):
    print("Age is " + str(age))

show_age(20)
