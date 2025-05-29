# Perform an element wise multiplication between 2 matrices using numpy
import numpy as np

A=np.array([[1, 2, 3], [4, 5, 6]])  
B=np.array([[5, 6, 7], [8, 9, 10]])  
result=np.multiply(A, B)
print(result)

# ---------------------------------------------------------------------------

# Reshape 2D array (6x6) into 3D array (4x3x3) using numpy
import numpy as np
import pandas as pd

a=np.arange(36).reshape(6, 6)
print("\n6x6 Matrix:",a)
b=a.reshape(4,3,3)
print("\nReshaped 4x3x3 Matrix:",b)

# ---------------------------------------------------------------------------

# write a program using numpy so that the result is inverse for example 42 gives 24

a=12
result=int(str(a)[::-1])
print("\nOriginal:",a)
print("Reversed:",result)

# ---------------------------------------------------------------------------

A=(("a", "b"),("a", "c"),("a", "d"),("b", "g"),("b", "s"),("e", "s"))
print("\nOriginal tuple: ",A)

a={}

for lst in A:
    key=lst[0]  
    if key not in a:
        a[key]=list(lst)  
    else:
        a[key].extend(lst[1:])  

New_A=tuple(a.values())
print("\nMerged Tuple:",New_A)