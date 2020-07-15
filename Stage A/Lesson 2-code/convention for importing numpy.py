# convention for importing numpy
import numpy as np

arr = [6, 7, 8, 9]
print(type(arr)) # prints <class 'list'>

a = np.array(arr)
print(type(a))  # prints <class 'numpy.ndarray'>
print(a.shape)  # prints (4,) - a is a 1d array with 4 items
print(a.dtype)  # prints int64

# get the dimension of a with ndim 
print(a.ndim)   # prints 1

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)        # prints [[1 2 3]
                         [4 5 6]]
print(b.ndim)   # prints 2
b.shape         # prints (2, 3) - b a 2d array with 2 rows and     3 columns
import numpy as np

arr = [6, 7, 8, 9]
print(type(arr)) # prints <class 'list'>

a = np.array(arr)
print(type(a))  # prints <class 'numpy.ndarray'>
print(a.shape)  # prints (4,) - a is a 1d array with 4 items
print(a.dtype)  # prints int64

# get the dimension of a with ndim 
print(a.ndim)   # prints 1

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)        # prints [[1 2 3]
                         [4 5 6]]
print(b.ndim)   # prints 2
b.shape         # prints (2, 3) - b a 2d array with 2 rows and     3 columns