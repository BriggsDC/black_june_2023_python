#Tuples as list elements
#city_1 = ('London', 'UK', 8.98) #City_1 through city_3 each represent 3 seperate variables
#city_2 = ('Canberra', 'Australia', 0.4)
#city_3 = ('Algiers', 'Algeria', 3.9)
#capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)] #This places each city variable in a single list. There are 3 elements inside the square bracket, each representing a tuple.
#You can work w/ such lists the usual way using a 'for' loop
#for capital in capitals:
    #print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])

#Lists in tuples
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5]) #This is an example of a list (i.e. the weight changes in kilos inside the square brackets) inside a tuple
Although tuples are 'immutable,' the list of kilo weight above inside the tuple is in fact mutable, so you can add new weight measurements to the list inside the tuple
user_data[3].append(79.6) #This adds an additional element at the end
print (user_data)

