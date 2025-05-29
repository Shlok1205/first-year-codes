import matplotlib.pyplot as plt

# Line plot
plt.figure()
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title("Line Plot")
plt.show()

# Bar plot
plt.figure()
plt.bar(['A', 'B', 'C', 'D'], [10, 20, 25, 30])
plt.title("Bar Plot")
plt.show()

# Pie chart
plt.figure()
plt.pie([10, 20, 25, 30], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Scatter plot
plt.figure()
plt.scatter([1, 2, 3, 4], [10, 20, 25, 30])
plt.title("Scatter Plot")
plt.show()
