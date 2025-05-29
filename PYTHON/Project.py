import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\hp\Desktop\programing\PYTHON\projmov2.csv")

# Data info 
print(df.info())
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.describe())  # Statistical summary
print(df.columns)  # Column names
print(df.shape)  # Rows and columns count
print(df.dtypes)  # Data types per column
print(df.isnull().sum())  # Count of nulls
print(df['Year of Release'].unique())  # Unique values
print(df.iloc[0:5, 0:3])  # First 5 rows and first 3 columns

# Plotting number of movies released each year
plt.figure(figsize=(10,6))
df['Year of Release'].value_counts().sort_index().plot(kind='bar')
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year of Release')
plt.ylabel('Number of Movies') 
plt.show()


# Plotting a bar plot for Budget and Box Office Collection for all movies in ascending order of amount
df.columns = df.columns.str.strip()

# Sorting the dataframe by 'Budget (USD)' in ascending order
df_sorted = df.sort_values(by=['Budget (USD)'], ascending=True)

plt.figure(figsize=(20,12))  # Set figure size
x = np.arange(len(df_sorted['Movie Name']))  # Label locations
width = 0.35  # Width of the bars

# Plotting Budget and Box Office Collection
plt.bar(x - width/2, df_sorted['Budget (USD)'], width, label='Budget', color='blue', alpha=0.7)
plt.bar(x + width/2, df_sorted['Box Office Collection (USD)'], width, label='Box Office Collection', color='red', alpha=0.7)

plt.title('Comparison Between Budget and Box Office Collection for All Movies (Sorted by Budget)', fontsize=16)
plt.xlabel('Movie Name', fontsize=14)
plt.ylabel('Amount in USD', fontsize=14)
plt.xticks(x, df_sorted['Movie Name'], rotation=90, fontsize=10)

# Adjusting y-axis to display values in billions
max_value = max(pd.to_numeric(df_sorted['Budget (USD)'], errors='coerce').max(), 
                pd.to_numeric(df_sorted['Box Office Collection (USD)'], errors='coerce').max())

# Adding data labels on top of the bars
for i, v in enumerate(pd.to_numeric(df_sorted['Budget (USD)'], errors='coerce')):
    plt.text(i - width/2, v + max_value * 0.01, f'${v:,.0f}', ha='center', fontsize=8, rotation=90)
for i, v in enumerate(pd.to_numeric(df_sorted['Box Office Collection (USD)'], errors='coerce')):
    plt.text(i + width/2, v + max_value * 0.01, f'${v:,.0f}', ha='center', fontsize=8, rotation=90)
if max_value and max_value >= 1e9:
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1e9:.1f}B'))
elif max_value and max_value >= 1e6:
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1e6:.1f}M'))

plt.legend(loc='upper left', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # Adjust layout for better visibility

# Ensure y-axis starts from the smallest value
plt.ylim(bottom=min(pd.to_numeric(df_sorted['Budget (USD)'], errors='coerce').min(), 
                    pd.to_numeric(df_sorted['Box Office Collection (USD)'], errors='coerce').min()))

plt.show()