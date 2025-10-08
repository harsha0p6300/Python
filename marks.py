def student(marks,attendance):
    if marks >=80:
        print("Good academic performance")
    else:
        print("Poor academic performance")
        if attendance >=75:
                 print("Eligeblie for scholarship")
        else:
         print("You are not eligible for scholarship")
marks=int(input("Enter your marks"))
attendance=int(input("Enter your attendance percentage"))
student(marks,attendance)