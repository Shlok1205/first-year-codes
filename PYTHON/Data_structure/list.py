list = [] # Empty list
list1 = [1,2,3,4,5] # List of integers
list2 = [1.1,2.2,3.3,4.4,5.5] # List of floats
list3 = ['one','two','three'] # List
list4 = ['Shlok', 25, [1,2,3], [5,0]] # Nested list
list5 = [100, 'Shlok', 12.432]
list6 = ['Shlok', 25, [1,2,3], [5,0],'Shlok','Arvind','Sanika','Chandni']
list7 = [1,(2,3),{4,5}]

print(list)
print(len(list))
print(list[1])

print(list1)       #slicing of list-HW
print(len(list1))
print(list[1])
print(list[1][0])

print(list2)
print(len(list2))

print(list3)
print(len(list3))

print(list4)
print(len(list4))

print(list5)
print(len(list5))

print(list6)
print(len(list6))

print(list7)
print(len(list7))
# ---------------------------------------------------------
list1.append(121005)
print(list1)

list2.append({'Shlok','Rudra','Arnav'})
print(list2)

list3.insert(9,'six')
print(list3)

for i in range(0,10):
    list1.insert(i,input())
print(list1)

list4.pop(2)
print(list4)

del list5[:]
print(list5)
# ----------------------------------------------------------

list1 = lista = [1,2,3,4,5]
listb = list1.copy()