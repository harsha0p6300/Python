def login():
    username=input("Enter your username")
    password=input("Enter your password")
    if username=="admin" and password=="1234":
        print("login succefully")
        role=input("Enter your role")
        if role=="admin":
            print("admin login succefully")
        else:
            print("invalid role")
    else:
        print("invalid username or password") 
login()
