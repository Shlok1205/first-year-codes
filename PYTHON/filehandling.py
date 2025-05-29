import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\hp\Desktop\programing\PYTHON\diabetic_data.csv')
print(df.info())
diabetic_data = df.shape
diabetic_data = df.iloc[:, 1:]
diabetic_data.loc = (diabetic_data['readmitted'] == 'NO')
diabetic_data.describe().T # Transposed df
diabetic_data.nunique() # Unique values in each column
diabetic_data.isnull().sum() # Null values in each column   