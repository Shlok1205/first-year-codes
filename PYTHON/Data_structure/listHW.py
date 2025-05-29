list1 = [1.0, 2.0, 3.0, 4.0, 5.0]  # Original list
lista = list1  # lista is assigned as list1
listb = list1.copy()  # listb is a copy of list1


print("Original lists:")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

# Operations on list1
list1.append(6.0)
print("After list1.append(6.0):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

list1.insert(2, 2.5)
print("After list1.insert(2, 2.5):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

list1.pop()
print("After list1.pop():")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

list1.clear()
print("After list1.clear():")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

list1.extend([7.0, 8.0])
print("After list1.extend([7.0, 8.0]):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

# ---------------------------------------------------------------

list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
lista = list1  # Re-assigning lista as list1
listb = list1.copy()  # Re-assigning listb as a copy of list1

print("Reset lists:")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

# Operations on lista
lista.append(7.0)
print("After lista.append(7.0):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

lista.insert(0, 0.5)
print("After lista.insert(0, 0.5):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

lista.pop()
print("After lista.pop():")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

lista.clear()
print("After lista.clear():")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

lista.extend([7.0, 8.0])
print("After lista.extend([7.0, 8.0]):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

# ---------------------------------------------------------------

list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
lista = list1  # Re-assigning lista as list1
listb = list1.copy()  # Re-assigning listb as a copy of list1

print("Reset lists:")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

# Operations on listb
listb.append(8.0)
print("After listb.append(8.0):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

listb.insert(0, -1.0)
print("After listb.insert(0, -1.0):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

listb.pop()
print("After listb.pop():")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

listb.clear()
print("After listb.clear():")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()

listb.extend([7.0, 8.0])
print("After listb.extend([7.0, 8.0]):")
print("list1:", list1)
print("lista:", lista)
print("listb:", listb)
print()