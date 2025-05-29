# import pandas as pd
# import numpy as np
# data = {'x': [78, 85, 96, 80, 86],
#         'y': [84, 94, 89, 83, 86],
#         'z': [86, 97, 96, 72, 83]}
# df = pd.DataFrame(data)

# print("Original DataFrame:")
# print(df)
# power_result = df['x']**df['y']**df['z'] 

# print("\nDataFrame after element-wise power operation:")
# print(power_result)

# ----------------------------------------------------------------------

# import pandas as pd
# import numpy as np
# n=3
# A = np.arange(9).reshape(3,3)
# B = np.arange(9).reshape(3,3)

# result = np.dot(A, B) #multiplication
# print("Mtrix multiplication: ")
# print(result)

# -----------------------------------------------------------------------

# import pandas as pd
# import numpy as np

# df = pd.read_csv(r'C:\Users\hp\Desktop\programing\PYTHON\book2.csv')

# print("First 3 rows of the DataFrame:")
# print(df.head(3))
# print(df.tail(3))
# print(df.describe()) #only giving data of numerical
# print(df.groupby('Score')['Attempts'].mean())
# print(df['Attempts'].mean())
# print(df['Attempts'].median())
# print(df['Attempts'].mode())
# print(df['Attempts'].min())
# print(df['Attempts'].max())
# print(df['Attempts'].std())
# print(df['Attempts'].var())
# print(df['Attempts'].count())
# print(df['Attempts'].sum())
# print(df['Attempts'].quantile(0.5))
# pd.read_csv('C:\\Users\\hp\\Desktop\\programing\\PYTHON\\book2.csv', skiprows=[1,3])
# dtype= {'Score': 'int', 'Attempts': 'int'}
# df = pd.read_csv('C:\\Users\\hp\\Desktop\\programing\\PYTHON\\book2.csv', dtype=dtype)
# Name = df['Name'].str.split(' ', expand=True)
# print(Name)
# # nrows = 100

# # ------------------------------------------------------------------------

# import pandas as pd
# import numpy as np

# data = {
#     'Column1': [1, 2, np.nan, 4],
#     'Column2': [np.nan, 5, 6, np.nan],
#     'Column3': [7, np.nan, np.nan, 10]
# }

# df = pd.DataFrame(data)

# print("Original DataFrame:")
# print(df)

# df.fillna(df.mean().astype(int), inplace=True)

# print("\nDataFrame after replacing missing values:")
# print(df)

# # -------------------------------------------------------------------------------

# # only for identity matrix

import pandas as pd
import numpy as np

a = np.array([[1, 2], [3, 4]])
b  = np.array([[5, 6], [7, 8]])

print(np.ones((2, 3)))
print(np.zeros((5, 6)))
print(np.eye(3))
print(np.eye(3, 4))
print(np.eye(3, 4, 0))
print(np.random.random((2, 3))) 
print(np.random.RandomState((2, 3))) 
print(np.random.default_rng((2, 3)))

# rand in random staticmethodrand in choice, normal and beta
# random.shuffle, det, rank, inverse, rant and identitiy matrix

print(a.diagonal())
print(a.T)
print(a.trace())
print(a.flatten())
print(a.ravel())
print(a.trace(), b.trace())
print(a.shuffle())
print(a.det())
print(a.rank())
print(a.inv())
print(a.rant())
print(a.identityMatrrix())
