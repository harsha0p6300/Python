# 1 Convert 1D array of 6 elements into 2×3 
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr.shape)
reshape=arr.reshape(2,3)
print(reshape)

# 2 Convert 8 elements into 2×4 
elements=np.array([2,3,4,5,6,7,8,9])
print(elements.shape)
reshapped=elements.reshape(2,4)
print(reshapped)

# 3 Write function for reshape
def reshape_fun(arr):
    ar=np.array(arr)
    shaped_arr=ar.reshape(2,4)
    return shaped_arr
print(reshape_fun([4,5,6,7,8,9,0,1]))

# 4 Create 3×2 matrix 
arr1=np.array([1,2,3,4,5,6])
matrix=arr1.reshape(3,2)
print(matrix)

# 5 Explain rows and columns after reshape 
# rows × cols = total elements
#   2  ×  3  =     6        ✅