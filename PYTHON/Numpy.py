import numpy as np

data = [1]  # Define 'data' as a list or appropriate structure
array = np.array(data)
print(array)
print(type(array))
print(array.ndim)
print(np.eye(4, 4, -1)) # Create a 4x4 identity matrix with a diagonal offset of -1

# ----------------------------------------------------------------------------------------

import numpy
a=[1,2,3,4] #module not found error (if not installed)
b = a
b = a[:2] #slice the array
b[0]=100
print(b) #[100   2]
print(a) #[100   2   3   4]
print(type(a)) #<class 'numpy.ndarray'>

# ----------------------------------------------------------------------------------------
import numpy as np
a1 = numpy.arange(16).reshape(4,4) # Create a 4x4 matrix with 16 elements
a1.fill(0)  
print(a1.ndim)
a2= a1[:2,:2] #slice the array
print(a2) 

# - --------------------------------------------------------------------------------------
import numpy as np
l = [1, 2, 3, 4]
A = np.array(l)
B = np.array([[10, 11, 17, 0], [5, 7, 9, 0]])  

# Broadcasting addition
np.add(A, B)
print("Addition with Broadcasting:")
print(A + B)

# Broadcasting multiplication
np.multiply(A, B)
print("Multiplication with Broadcasting:")
print(A * B)

# Broadcasting with a scalar
scalar = 2
print("Broadcasting with Scalar Multiplication:")
print(A * scalar)

# - --------------------------------------------------------------------------------------
import pandas as pd
import numpy as np

A = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
B = np.array([5, 6, 7, 8, 9, 10]).reshape(3, 2)
result = np.dot(A, B)

# Convert the result to a pandas DataFrame for better readability
df_result = pd.DataFrame(result, columns=["Col1", "Col2"])
print("Result as a Pandas DataFrame:")
print(df_result)

# ----------------------------------------------------------------------------------------

import numpy as np
array = np.array([1,2,3,4])
total_sum = np.sum(array) 
print("Total Sum:", total_sum)

# -----------------------------------------------------------------------------------------


