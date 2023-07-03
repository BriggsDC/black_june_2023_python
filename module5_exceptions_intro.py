
#value = int(input('Enter and integer: '))
#print('The inverse of', value, 'is', 1/value) 

#An “unwanted event” is when the user inputs something else besides a integer; its something that you don’t expect. 
#In the event of an “unwanted error,” Python will “raise an exception” and stop the program.
#In order to handle exceptions, you’ll need to use “try: except:”
#try: #You'd'insert the key word 'try'
    #value = int(input('Enter and integer: '))
    #print('The inverse of', value, 'is', 1/value) #Here is where the user could input code that raises an exception
#except: #You'd also enter the key word 'except'
    #print('You did not provide a number, so I will not calculate the inverse') #Here is where you handle the exception; this is what you decide to do if/when an exception is raised
    
#Note the ZeroDivisionError and ValueError
try: 
    value = int(input('Enter and integer: '))
    print('The inverse of', value, 'is', 1/value) 
except ValueError: #Note that the exception name is specified
    print('You did not provide a number, so I will not calculate the inverse') 
except ZeroDivisionError: #Note that this is the second exception
    print('Sorry, you provided the number 0, and division by 0 is not possible') 

#This is a 'general' exception w/ no specific exception name
try: 
    value = int(input('Enter and integer: '))
    print('The inverse of', value, 'is', 1/value) 
except ValueError: 
    print('You did not provide a number, so I will not calculate the inverse') 
except ZeroDivisionError: 
    print('Sorry, you provided the number 0, and division by 0 is not possible') 
except: #Note that this is the third exception. This will be used in the event any other exception besides the ones above are raised. It is a default except block
    print('Sorry, something strange happened here') 





