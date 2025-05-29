x=('Shlok Madan')
print(x)
print(x[10]) #idexing starts at 0. So,the 10th index correspoinds to 11th charecter.
print(x[2:5])#This is slicing. It extracts charecters from index 2 to 4
print(x[1:0])#This slice is invalid because the start index 1 is greater than the end index 0. 
#Slicing in python works only when the start index is lessthan or equal to the end index.
print(x[-1])#negetive indexing starts from the end of the string. Here, -1 refers to the last character, which is n. 
print(x[-1:2])
print(x[-1:-2])#This slice is invalid because slicing moves left to right, But here the start index -1 is greater than the end index -2.
print(x[2:4:5])
print(x[-1:-2:-1])#This slice works because of the negetive step -1, which reverse the direction of slicing
#it starts at index -1(last charecter n) and moves to index -2(but does not include it)
print(x[2:-1])#this slice starts at index 2 and goes upto the second last charecter
print(x[2:4:5])
print(x[-1:2:4])
print(x[0:1:2])
print(x[-1:0:1])


#Why Doesn't Python Throw an Error?
#Python slicing is designed to be graceful and avoids runtime errors in these scenarios. Instead, it just returns an empty string because:
#No characters match the slicing criteria.
#It assumes this is a valid but empty result.

