import numpy as np
# 1 Create array of 5 marks and find average marks 
marks=[34,55,61,70,77]
print(np.average(marks))

# 2 Find average temperature of one week data
temp=[27,30,32,40,42]
print(f"The average temp is {np.average(temp)}C")

# 3 Write a function to calculate average of array 
def array_fn(array):
    arr=np.average(array)
    return arr
print(array_fn([30,45,50,77]))

# 4 Create array [12,18,24,30] and find mean 
air=[12,18,24,30]
print(np.mean(air))

# 5 Compare average of two arrays 
a1=[12,18,24,30]
a2=[13,19,25,31]
print(f"The average of a1 is {np.average(a1)}")
print(f"The average of a2 is {np.average(a2)}")
print("arr1 > arr2",np.average(a1)>np.average(a2))