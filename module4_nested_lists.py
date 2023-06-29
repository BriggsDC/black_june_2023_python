#Just like nested loops, Python offers nested lists. Lists are generally a collections of multiple elements
#numbers = [1, 2, 3, 4] #This is a list w/ integer values; each element in this list is an integer
#countries = ['UK', 'US', 'Germany'] #This is a list w/ string values; each element in this list is a string
#countries = [1, 'UK', 2, 'US'] #Python even allows you to mix multipple data types w/ in a single list. However, this is NOT recommended and you should void it. All elements of a list should have the same data type

#Lists can also have other lists as elements
#cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']] #The outer list named 'cells' contains 2 elements inside; the first and second elements have 3 strings inside

#To access the first element w/ index 0, you'll get a sub-list in retun
#cells[0]

#To access a specific element in the sub-list
#cells[0][0]

#A 'for' loop iterates the list and prints its elements 
#cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']] 
#for x in cells:
    #print('Element:', x)

#To access the individual string elements inside the sub-lists (i.e. A1 or A2 individually), use 'nested for loops'. AKA 'multi-dimensional lists,' they are used to represent multidimensional objects like tables; multi-dimensional lists are lists w/in lists, 1 or 2 lists are the most common
#cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']] 
#for x in cells: #In the first iteration 'x' is the  first element in the list, which is a list. Since 'x' is a list itself, you can use a 'for' loop again to get individual items in the sublist
    #for y in x:
        #print('Element:', y)

#Can be applied to write to tables; note the name changes below (i.e. row, table); the output is the same as above
#table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']] 
#for row in table: #In the first iteration 'x' is the  first element in the list, which is a list. Since 'x' is a list itself, you can use a 'for' loop again to get individual items in the sublist
    #for cell in row:
        #print('Element:', cell)
        
#You can also print the elements in such a way that they do resemble a table
#table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']] 
#for row in table: #In the first iteration 'x' is the  first element in the list, which is a list. Since 'x' is a list itself, you can use a 'for' loop again to get individual items in the sublist
    #for cell in row:
        #print(cell, '', end='')
    #print()
    
#To initialize a list that looks like the one  w/ the same values:
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

#Do the following:
table = [[i for i in range(1, 6)] for j in range(4)] #Note that the 'inner list' comprehension places the 'i' control variable value before the 'for loop;' the 'outer list' comprehension means repeat the inner list comprehension until the control variable of 'j' reaches the value of '4' 
print(table)

