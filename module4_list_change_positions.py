#You save the value of the first variable to the temporary third variable so you don’t lose it.
#first = input('Enter first number: ')
#second = input('Enter second number: ')
#print('Before swapping:', first, second)
#temporary = first #This is the temp third value
#first = second
#second = temporary
#print('After swapping:', first, second)

#Python has an alternative shotcut. 
#first = input('Enter first number: ')
#second = input('Enter second number: ')
#print('Before swapping:', first, second)
#first, second = second, first
#print('After swapping:', first, second)

#The same logic above can be used for lists where you can swap elements 
#top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
#print(top_cities)

#You can also sort list elements alphabetically using '.sort()'
#top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#top_cities.sort()
#print(top_cities)

#You can also sort list elements numbers from the lowest to the greatest using '.sort()'
#random_numbers = [2, 5, 0, -3, 4]
#random_numbers.sort() #Remember 'sort' is a method changing the 'list' it belongs to. It cant be undone easily.
#print(random_numbers)

#You can also sort list elements numbers from the greatest to the lowest using a keyword argument 
# = [2, 5, 0, -3, 4]
#random_numbers.sort(reverse=True) #Note the keyword argument, numbers will get sorted from the greatest to the lowest. Also, remember 'sort' is a method changing the 'list' it belongs to
#print(random_numbers)

#This is a 'general list function' instead of a list method, where you can keep the original list and the sorted list temporarily
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities) #This is the original sorted elements



