# 1 Remove duplicates from [1,2,2,3,4,4,5]
import numpy as np
num=[1,2,2,3,4,4,5]
print(np.unique(num))

# 2 Count unique elements 
el=[1,2,4,2,4,5,6,6,8,9,9]
u_values=np.unique(el)
print(len(u_values))

# 3 Write function using unique() 
def unq(num):
    return np.unique(num)
print(unq([2,4,5,6,7,5,6,7]))

# 4 Remove duplicates from student IDs 
ids = [101, 102, 103, 101, 104, 105, 102, 106, 107, 105, 108, 109, 110, 108]
print(np.unique(ids))

# 5 Compare original and unique array 
id=[2,4,5,6,7,5,6,7]
Unq=np.unique(id)
print("Duplicates Removed",len(id)-len(Unq))