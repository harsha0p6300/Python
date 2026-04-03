import numpy as np
# 1 Sort [45,12,78,9,34] 
S=[45,12,78,9,34] 
print(np.sort(S))

# 2 Sort marks in ascending order
marks=[35,40,38,67,81]
print(np.sort(marks))

# 3 Sort salary data 
salary=[18000,13000,17000,25000]
print(np.sort(salary))

# 4 Write function to sort array 
def arr(num):
    return np.sort(num)
print(arr([35,78,23,99,5,44]))

# 5  Sort and print highest value separately
import numpy as np 
high=[35,40,38,67,81]
print(np.sort(high))
print(f"The highest value of the list is {np.max(high)}")