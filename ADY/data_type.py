user=input("enter some value :")

if user.isdigit():
    print("its an integer")
elif "." in user and user.replace(".","").isdigit():

    print("its an float")
else:
    print("it is a string")

type(3+5j)







