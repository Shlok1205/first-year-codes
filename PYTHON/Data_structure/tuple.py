# mytuple=() #initializing an empty tuple
# print(type(mytuple))

# tuple1=(1,2,3,4,5) #integer data type
# print(tuple1)

# tuple2=("Shlok","Arvind","Chandni","Sanika") #string data type
# print(tuple2)

# tuple3=(12.2,17.3,19.4,21.5) #float data type
# print(tuple3)

tuple4 = ("Shlok", 12, ("Arvind", 17.3, "Chandni", 19), "Sanika", 21.5)
print(tuple4)

# for i in tuple4: print(tuple4.index(i),i)


# print(tuple4[0:4])  
# print(tuple4[4:8])  
# print(tuple4[-1:1:-1])  

nested_tuple = tuple4[1]
print(nested_tuple)  
for j in range(len(nested_tuple)):
    print(j, nested_tuple[j])


# tuple5=(11,3,45.5,{"Shlok","Arvind","Chandni","Sanika"},[1,2,3,4,5],(1,2,3,4,5))
# print(tuple5)

# a=(1,2,3,4,5)  
# b=(1.944,99,3,35,5.43) 
# print(a+b)
# print(a*3)
# print((a))*3

