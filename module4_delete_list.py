top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[2] #Just type 'del' and insert the element(s) you want to delete. Once an element is deleted, all values to the right are shifted to the left.
print(top_cities)

top_cities[2] #Running this should now display a new element, 'Chicago' 


top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[3:] #This keeps the first 3 elements of the list and deletes the remaining ones using 'del' AND 'slicing' in a single operation; starts at index 3 onward; it means delete all elements starting at index 3 until the end of the list, leaving the first 3 elements intac (0, 1 and 2 are still included in the list)
print(top_cities)

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix'] 
del top_cities[:] #You can also delete all elements from a list using a slice w/ both indices omitted; you should get an empty [ ] in return
print(top_cities)


top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix'] 
del top_cities #You can delete an entire list by providing its name w/out any indices
print(top_cities) #You will likely get an error due the variable no longer being available

#Note that 'del' is not a function call, it is an instruction. Functions require a function call followed by a pair of square brackets 

