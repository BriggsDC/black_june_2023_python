#'Lists' are usually used to store multiple values of the same type (i.e. multiple integers, floats or strings)
city_1 = 'New York City'
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix'
 
#It is much easier to use a single variable w/ a list inside, instead of a list of individual variables being assigned.
empty_list = [ ]

#Elements in a list are numbered; New York is the first element, Los Angeles is the second element, etc. Also, each element has a unique numerical index you can use to get the element out. The first element of a list starts at 0 NOT 1.
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#print(top_cities)

#To get a specific element and not a whole list, provide the element index inside the square bracket; this is called 'indexing.' Attempting to access an element that doesn’t exist will return an ‘IndexError.’
#top_cities[0] #This displays the first element
#top_cities[1] #This displays the second element

#You can also use ‘negative indices.’ An index w/ a minus 1 gives you the last element from the list. You can only go as far as the amount of elements in a list; so this list cannot exceed -5
#top_cities[-1] #This displays the last element from the end of the list
#top_cities[-2] #This displays the second element from the end of the list

#'Slicing' enables you to access a few, but not necessarily all elements at the same time. Slicing gets the first 2 elements.
top_cities[0:2] #The colon is used here to introduce indices. It represent the first element to include into the slice, and the second element to NOT include into the slice; the first index is inclusive, the second one is exclusive. For this example, you'd use index 0 and index 1
['New York', 'Los Angeles']


top_cities[2:] #If you omit the first index, it means from the start of the list; if you omit the second index it means until the very end of the list. This means take all elements starting at index 2 until the very end of the list

top_cities[:3] #This means take all elements of the list from the start untik the index 3, exclusively

top_cities[:] #This omits both, meaning all of the elements. It is the same as 'top_cities' w/ out an element
