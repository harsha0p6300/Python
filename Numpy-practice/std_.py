# 1 Find std of [10,20,30,40,50] 
import numpy as np
a=[10,20,30,40,50]
print(np.std(a)) 

# 2 Compare std of two arrays 
a1=np.std([10,20,30,40,50])
a2=np.std([29,78,39,47,55])
print(a1,a2)
print("a1>a2",a1>a2)

# 3 Write function for std 
def strandard_deviation(num):
    return np.std(num)
print(strandard_deviation([29,78,39,47,55]))

# 4 Which array has more spread? 
array1=[28,29,30,31,32]
array2=[10,30,50,20,40]
print(np.std(array1))
print(np.std(array2))
if (np.std(array1))>(np.std(array2)):
    print("The array1 Has a more spread")
else:
    print("The Array2 Has more spread")

# 5 Explain result in words