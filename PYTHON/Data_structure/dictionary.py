d = {}
d = set()
d = {"Name":{"Shlok","Chandni","Arvind","Sanika"},"Age":{'19','42','45','19'}}
print(d)

print(type(d)) # <class 'dict'>

print(len(d)) # 2

for i in d:
    print(i) # Name, Age

print(d["Name"]) # {'Shlok', 'Chandni', 'Arvind', 'Sanika'}

print(d.get("Name")) # {'Shlok', 'Chandni', 'Arvind', 'Sanika'}

print(d["Age"]) # {'19', '42', '45'}

print(d.get("Age")) # {'19', '42', '45'}

print(d.keys)   # prints address

print(d.keys()) # dict_keys(['Name', 'Age'])

print(d.values()) # dict_values([{'Shlok', 'Chandni', 'Arvind', 'Sanika'}, {'19', '42', '45'}])

print(d.items()) # dict_items([('Name', {'Shlok', 'Chandni', 'Arvind', 'Sanika'}), ('Age', {'19', '42', '45'})])

d["Name"] = "Kevin" # {'Name': 'Kevin', 'Age': {'19', '42', '45'}}

print(d.values()) # dict_values(['Kevin', {'19', '42', '45'}])
print(d) # {'Name': 'Kevin', 'Age': {'19', '42', '45'}}

for i in enumerate(d.keys()): 
    print(i) # (0, 'Name') (1, 'Age')

popped_item = d.pop("Age") # {'Name': 'Kevin'}
print("Popped item:", popped_item) # Popped item: {'19', '42', '45'}
print(d) # {'Name': 'Kevin'}

popped_item = d.popitem() 
print("Popped item:", popped_item) # Popped item: ('Name', 'Kevin')
print(d) # {}

# d.clear() # {}
# print(d) # {}
print(len(d))  # 0
