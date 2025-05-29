import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\hp\Desktop\programing\PYTHON\movies_list_pyproject.csv")

# Print basic information
print(df.info())
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.describe())  # Statistical summary
print(df.columns)  # Column names
print(df.shape)  # Rows and columns count
print(df.dtypes)  # Data types per column
print(df.isnull().sum())  # Count of nulls
print(df['Year of Release'].unique())  # Unique values
print(df['Box Office Collection (USD)'].value_counts())  # Frequency count

# Plotting a bar plot for Year of Release
plt.figure(figsize=(10, 6))  # Set the figure size
df['Year of Release'].value_counts().sort_index().plot(kind='bar')  # Create a bar plot
plt.title('Number of Movies Released Each Year')  # Title of the graph
plt.xlabel('Year of Release')  # X-axis label
plt.ylabel('Number of Movies')  # Y-axis label
plt.show()

# Cleaning and converting the columns for Budget and Box Office Collection
df['Budget (USD)'] = df['Budget (USD)'].replace({'\$': '', ',': '', 'million': 'e6', 'billion': 'e9'}, regex=True).map(pd.to_numeric, errors='coerce')
df['Box Office Collection (USD)'] = df['Box Office Collection (USD)'].replace({'\$': '', ',': '', 'million': 'e6', 'billion': 'e9'}, regex=True).map(pd.to_numeric, errors='coerce')


# ------------------------------------------------------------------------------------------------------------------------------------
# Combined Line Plot for Budget and Box Office Collection
# plt.figure(figsize=(10, 6))
# df_sorted = df.sort_values('Year of Release')  # Sort by Year of Release for better visualization
# plt.plot(df_sorted['Year of Release'], df_sorted['Budget (USD)'], label='Budget (USD)', marker='o')
# plt.plot(df_sorted['Year of Release'], df_sorted['Box Office Collection (USD)'], label='Box Office Collection (USD)', marker='x')
# plt.title('Comparison of Budget and Box Office Collection Over the Years')
# plt.xlabel('Year of Release')
# plt.ylabel('Amount (USD)')
# plt.legend()
# plt.grid(True)
# plt.show()


plt.figure(figsize=(12, 8))
df_sorted = df.sort_values('Year of Release')  # Sort by Year of Release for better visualization

# Plot Budget and Box Office Collection
plt.plot(df_sorted['Year of Release'], df_sorted['Budget (₹ Crore)'], label='Budget (₹ Crore)', marker='o', linestyle='-', color='blue')
plt.plot(df_sorted['Year of Release'], df_sorted['Box Office Collection (₹ Crore)'], label='Box Office Collection (₹ Crore)', marker='x', linestyle='--', color='green')

# Enhance the graph with labels and title
plt.title('Budget vs Box Office Collection Over the Years')
plt.xlabel('Year of Release')
plt.ylabel('Amount (₹ Crore)')
plt.legend()
plt.grid(True)
plt.show()
