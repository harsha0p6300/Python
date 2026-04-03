user=input("Enter some random value: ")

if user.isdigit():
    print("Its an integer")
elif "." in user and user.replace(".","").isdigit():
    print("its an float ")
else:
    print("its an string")