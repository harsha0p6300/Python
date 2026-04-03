import numpy as np
# 1.Create an array of 5 student marks and find total marks using sum() 
marks=np.array([35,42,59,91,88])
print(np.sum(marks))

# 2.Create an array of prices [100, 250, 300, 450] and find total bill amount 
prices=[100,250,300,450]
bill=np.sum(prices)
print(f"The Total Bill is {bill}")

# 3.Create an array [5,10,15,20,25] and calculate total
l=[5,10,15,20,25] 
print(f"The Total is {np.sum(l)}")

#4. Write a function to calculate sum of an array
def summ_array(array):
    total=np.sum(array)
    return total
print(summ_array([3,5,6,8]))

#5.  Create two arrays and find sum of both arrays separately 
import numpy as np
a1=[1,2,3,4,5]
a2=[10,20,30,40,50]
total1=np.sum(a1)
total2=np.sum(a2)
print(f"The sum of 1st array is {total1}")
print(f"The sum of snd array is {total2}")
