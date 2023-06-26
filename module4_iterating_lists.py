#top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'] #Indexes 0 through 4
#for city in top_cities #A 'for' loop was used to access the list elements 1 by 
        #print('Current city:', city) #The control variable 'city' was defined; you can use your own variable name here
   
#top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
#for city_index in range(len(top_cities)): #'len' returns the number of characters for 'strings' BUT returns the number of 'elements' for 'lists' (i.e. 5 cities in the below list); 'range(5)' will generate the following numbers 'returs[0,1,2,3,4]'
        #print('Current index:', city_index, '| Current city:', top_cities[city_index], ) #'city_index' is the control variable for the given index
         
#spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
#sum = 0.0 #This is the initial variable of 'sum'
#for spending in spendings:
    #sum += spending
#print('Money spent:', sum) #This sums up all the numbers in the list      
         
         
         
#John has a hard time keeping his budget. Write a program to help him analyse his spendings. You are given a list with John's spendings for each month. 
#Go through the list, and count the number of times...
#a. the spendings were low (< 1000.0)
#b. the spendings were normal (between 1000.0 and 2500.0 inclusive)
#c. the spendings were high (> 2500.0)
#Then, print the following to the output:
#Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.

spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
 
low = 0
normal = 0
high = 0
 
for month in spendings:
    if month < 1000.0:
        low += 1
    elif month <= 2500.0:
        normal += 1
    else:
        high += 1
 
print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(normal) + ', high spendings: ' + str(high) + '.')
      