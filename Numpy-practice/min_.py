# 1 Find lowest mark from student marks 
import numpy as np
marks=[35,67,29,19]
print(np.min(marks))

# 2 Find minimum temperature
temp=30,45,46,49
print(np.min(temp))

# 3 Write function for minimum value 
def min_(num):
    return np.min(num)
print(min(3,6,7,8,9,10))

# 4 Find smallest value in [45,12,78,9] 
array=[45,12,78,9]
print(np.min(array)) 

#5 Compare lowest values of two arrays
a1=[13,15,8,22,33]
a2=[11,5,18,24,36]
low1=np.min(a1)
low2=np.min(a2)
print(low1,low2)
print("a1>a2",a1>a2)
