#This copies a list into a new variable. I applies to other basic data types such as integers, floats and Booleans but the same rule is NOT true for data collections like lists; lists are a complex data type 
#name_original = 'Jon Snow' #This line takes the string value stored under the name of the first variable and copies it under the 'name' new
#name_new = name_original #Has the same value, yet they are each independent; if you change one of the values, it will not effect the other one
#name_original = 'Daenerys Targaryen'
#print(name_original, name_new)

#'Slicing' makes a copy of a list where 2 variables have 2 seperate lists that you can modify independently
#list_original = [1, 2, 3]
#list_new = list_original [:] #This indicates 'slicing' from the very beginning to the end of the list
#list_original[0] = -5
#print('Original:', list_original, '\\nNew:', list_new)

#'Slicing' can copy a specific number of elements to a new list
#list_original = [1, 2, 3]
#list_new = list_original [:2] #This 'slicing' copies the 2 first elements from the original list to a new list
#list_original[0] = -5
#print('Original:', list_original, '\\nNew:', list_new)

#To copy a list and have 2 different lists and 2 different variables
list_original = [1, 2, 3]
list_new = list_original [:] 
print('Original:', list_original, '\\nNew:', list_new)




