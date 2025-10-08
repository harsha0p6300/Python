def python(lang,exp):
    if lang=="python":
        print("yes you are using python")
        if int (exp)>2:
           print("you are experienced programmer")
        else:
           print("you are not experienced")
    else: 
           print("you are not using python")
lang,exp=input("Enter the language you are using and your experience in years").split()
check_skills(lang,exp)