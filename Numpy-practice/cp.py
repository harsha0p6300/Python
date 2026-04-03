# # 1 Create one program showing mean, sum, max, min 
import numpy as np
data=np.array([3,5,6,12,10])
average=np.mean(data)
summ=np.sum(data)
maxm=np.max(data)
minm=np.min(data)
print(f"The Mean of your data is {average}")
print(f"The Total of your data is {summ}")
print(f"The highest Element in your data is {maxm}")
print(f"The Lowest element in your data is {minm}")

# # 2 Create one function for all statistics
def all_statistics(data):
    ar=np.array(data)
    average=np.mean(ar)
    Total=np.sum(ar)
    High=np.max(ar)
    low=np.min(ar)
    mediun_=np.median(ar)
    stndard_d=np.std(ar)
    var_=np.var(ar)
    print("The total of the data is",Total)
    print("The average of the data is:",average)
    print("The Highest element of the data is:",High)
    print("The low of the data is:",low)
    print("The meduian of the data is:",mediun_)
    print("The standrd_deviation is",stndard_d)
    print("The varience is:",var_)

all_statistics([2,3,4,5,6,8])

# # 3 Input marks and show all statistics 

def all_statistics(user):
    ar=np.array(user)
    average=np.mean(ar)
    Total=np.sum(ar)
    High=np.max(ar)
    low=np.min(ar)
    mediun_=np.median(ar)
    stndard_d=np.std(ar)
    var_=np.var(ar)
    print("The total of the data is",Total)
    print("The average of the data is:",average)
    print("The Highest element of the data is:",High)
    print("The low of the data is:",low)
    print("The meduian of the data is:",mediun_)
    print("The standrd_deviation is",stndard_d)
    print("The varience is:",var_)

marks=[int(input(f"Enter marks you scored in 5 subs: {i+1} ")) for i in range(5)]
all_statistics(marks)


# 4 Compare two arrays statistics 

student1=([1,3,5,7,11])
student2=([2,4,6,8,10])
marks1=np.array(student1)
marks2=np.array(student2)
print("The student 1 average is good than student2",np.average(marks1)>np.average(marks2))
print("The Highest marks secured S1 not S2",np.max(marks1)>np.max(marks2))
print("The Lowest scored is S1<s2",np.min(marks1)<np.min(marks2))
print("The more consistent is s1>s2",np.std(marks1)>np.std(marks2))