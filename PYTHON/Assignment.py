# Python script demonstrating operations on different data structures

# Working with LISTS
print("\nLIST OPERATIONS")
my_list = [1, 2.5, 3]
print("Initial List:", my_list)

# Adding elements
my_list.append(4)
my_list.append(5.5)
print("After Appending:", my_list)

# Inserting elements at specific positions
my_list.insert(1, 10)
my_list.insert(2, 2.8)
print("After Inserting:", my_list)

# Removing elements
my_list.remove(10)
print("After Removing 10:", my_list)

# Popping elements
my_list.pop()
print("After Popping Last Element:", my_list)

# Clearing the list
my_list.clear()
print("After Clearing List:", my_list)

# Working with TUPLES
print("\nTUPLE OPERATIONS")
my_tuple = (1, 2.5, 3, 1, 2.5)
print("Tuple:", my_tuple)

# Counting occurrences
print("Count of 1:", my_tuple.count(1))
print("Count of 2.5:", my_tuple.count(2.5))

# Finding indexes
print("Index of 1:", my_tuple.index(1))
print("Index of 2.5:", my_tuple.index(2.5))

# Working with SETS
print("\nSET OPERATIONS")
my_set = {1, 2.5, 3}
print("Initial Set:", my_set)

# Adding elements
my_set.add(4)
my_set.add(5.5)
print("After Adding Elements:", my_set)

# Removing elements
my_set.remove(1)
print("After Removing 1:", my_set)

# Popping an arbitrary element
my_set.pop()
print("After Popping an Element:", my_set)

# Clearing the set
my_set.clear()
print("After Clearing Set:", my_set)

# Updating the set
my_set.update([10, 20])
print("After Updating Set:", my_set)

# Working with DICTIONARIES
print("\nDICTIONARY OPERATIONS")
my_dict = {1: "one", 2.5: "two point five", 3: "three"}
print("Initial Dictionary:", my_dict)

# Adding key-value pairs
my_dict[4] = "four"
my_dict[5.5] = "five point five"
print("After Adding Keys:", my_dict)

# Removing a key
my_dict.pop(1)
print("After Popping Key 1:", my_dict)

# Clearing the dictionary
my_dict.clear()
print("After Clearing Dictionary:", my_dict)

# Updating the dictionary
my_dict.update({6: "six", 7.5: "seven point five"})
print("After Updating Dictionary:", my_dict)

# Displaying keys and values
print("Dictionary Keys:", list(my_dict.keys()))
print("Dictionary Values:", list(my_dict.values()))
