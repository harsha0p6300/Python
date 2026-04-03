import numpy as np
# 1 Find highest mark from 5 student marks
marks=[45,66,70,81,88,89]
print(f"The highest marks of the student is {np.max(marks)}")

# 2 Find maximum salary from salary list
salary=[17000,5000,16000,55000]
print(f"The maximun salary from the salary list is {np.max(salary)}")

# 3 Create function to find maximum number 
import numpy as np
def maxinum(n):
    return np.max(n)
print(maxinum([3,6,8,9]))

# 4 Find highest value in [25, 67, 89, 34] 
value=[25,67,89,34]
print(f"The highest value is {np.max(value)}")

# 5. Compare max value between two arrays 
a1=[25,67,89,34]
a2=[45,66,70,81]
arr1=np.max(a1)
arr2=np.max(a2)
print(arr1)
print(arr2)
print("The arr1>arr2",arr1>arr2)