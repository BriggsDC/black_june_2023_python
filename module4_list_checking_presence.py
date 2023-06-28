#Here the 'in' operator is requesting every element of the 'for' loop to be checked
#for char in 'happy message': 
    #print(char)

#The 'in' operator can also be used to check whether a given element is present in a list
#invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
#name = input('What is your name? ')
#if name in invited_guests:
     #print('Welcome!')
#else:
    #print('You are not invited!')

#This is an example of a negated operator, 'not 'in'' It returns 'True' if the element is not found on the list. Similar to the above example, but reversed.
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')
   
