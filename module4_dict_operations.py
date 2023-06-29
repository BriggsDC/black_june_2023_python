#Starting w/ an empty dictionary and adding elements to it
#grades = {} #This alone (i.e. the curly brackets) creates an empty dictionary. Here you created an empty dictionary and added 2 entries
#grades['John'] = 'A-' #Using square brackets [ ] adds new elements
#grades['Anne'] = 'B'
#print(grades)

#You can update dictionary entries using the very ame syntax
#grades['Anne'] = 'A' #Anne retook an exam and recieved a better grade
#print(grades)

#Another option is to use the 'update method'
#grades.update({'John':'A'})
#print(grades)

#To check the number of key value person in a dictionary, use the 'len' function
#len(grades)
#print(len(grades))

#To check if a given key is present in a dictionary, use the 'in' operator
#if 'John' in grades:
    #print('John got:', grades['John'])

#To delete a given key along side its value, use the 'del' operator
#del grades['John']
#print(grades)

#You can iterate a dictionary (dictionaries are now ordered collections by default)
#You can use a simple 'for' loop to access dictionary keys
grades = {} 
grades['John'] = 'A-' 
grades['Anne'] = 'B'
#for el in grades: #This prints the keys to the ouput
    #print(el)

#You can achieve the same output as above using the 'keys method' 
#for el in grades.keys(): #This prints the keys to the ouput
    #print(el)

#To access the values and the values alone...
#for el in grades.values(): #This will show you only the values of the output
    #print(el)

#To access BOTH the keys and values, use the 'item' method
for person, grade in grades.items():
    print(person, 'got', grade)






