# 1 Find variance of [5,10,15,20] 
import numpy as np
arr=[5,10,15,20]
print(np.var(arr))

# 2 Compare variance of two arrays 
a1=np.var([5,10,15,20])
a2=np.var([9,16,22,32])
print(a1,a2)
print("The varience of a1>a2 is ",a1>a2)

# 3 Write function for variance 
def variance(num):
    return np.var(num)
print(variance([5,10,15,20]))
# 4 Explain why variance is useful 
# 5 Find variance of marks dataset 
data=[35,40,60,75,90]
print(np.var(data))