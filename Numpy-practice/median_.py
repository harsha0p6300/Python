#1 Find median of [10,20,30,40,50] 
import numpy as np
l=[10,20,30,40,50]
print(np.median(l))

#2 Find median of odd numbers array
odd=[3,11,15,19,23]
print(np.median(odd))

#3 Find median of even numbers array 
even=[2,12,16,20,24,26]
print(np.median(even))

#4 Write function for median 
def med(num):
    return np.median(num)
print(med([3,5,13,16,17,22]))

# 5 Compare mean and median in same array 
data=[2,5,7,13,16,18]
print(np.mean(data),np.median(data))
print("mean>median",np.mean(data)>np.median(data))
