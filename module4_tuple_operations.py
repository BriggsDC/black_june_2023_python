#The 'len' function counts the number of elements in a tuple
#user_data = ('John', 'American', 1964)
#print(len(user_data))

#You can use the 'in' and 'not in' operators the same as you would for lists
#user_data = ('John', 'American', 1964)
#if 'American' in user_data:
    #print('This person comes from the US!')

#You can also iterate a tuple w/ a 'for' loop
#user_data = ('John', 'American', 1964)
#for element in user_data:
    #print(element)
   
#Just like strings, tuples can be added together or multiplied by an integer
#user_data = ('John', 'American', 1964) +  ('teacher', 'male') #This essentially creates a new tuple w/ the same elements
#print(user_data)

#numbers = (0, 1) * 10 #The elements will repeat 10 times
#print(numbers)

#Lists are typically used when you want to have many values of the same data type; they are used when the values represent examples of the same class or phenomenon. See below examples:
male_name = ['Adam', 'Jerry', 'Mark'] #Each element is a string that represents a male's name
berlin_temps = [13.0, 17.5, 12.0] #Each element is a float that represents a temperature in Berlin

#Tuples are used when you want to group values of different types that are somehow related, that together form some sort of structure, or bigger data.
user_data = ('John', 'American', 1964) #This is 3 elements of different data types. The name and nationality are strings and the year born an integer, however, all 3 are somehow related. They all describe 1 user.

#Tuples are often used to perform certain Python operations quicker.
first = 5
second = 7
first, second = second, first #Both are tuples; they can appear on the left and right side of the assigment operator. Note that tuple elements can be variables; 'first' and 'second' are variables.

