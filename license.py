def criteria(age, eye_test):
    if (age)>=18:
        print("age criteria met")
        if eye_test:
              print("ELIGIBLE FOR DRIVING LICENSE")
    else:
        print("You are not eligible for driving license")
age=int(input("Enter your age"))
eye_test=input("enter eyes test true or false")
criteria(age,eye_test)
