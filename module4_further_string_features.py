#Like lists, strings are sequences. You can use indexing and slicing w/ strings to read individual characters or groups of characters
#fav_band = 'Green Day'
#print(fav_band[6])

#print(fav_band[:6]) #Means from the beginning until index 6; this returns the first 6 letters

#Note that you cannot use indexing to change individual characters w/in a string
#fav_band[6] = 'M' #This will not work; it will return an error

#Just like lists, strings in Python have many built-in methods (see https://docspython.org for more)
#text = 'Please capitlize me'
#text_cap = text.upper() #This method transforms a string and somehow returns a new string back (i.e. upper and lower)
#print(text_cap) 

#This string method returns 'True' or 'False'
user_number = input('Please provide a number: ')  #'isnumeric' checks whether your string contains digits only; this is helpful when using the input function because it can check whether a user is entering a number correctly
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!') #'if' number is numeric, print this
else:
    print('Sorry,', user_number, 'is not a number!') #Otherwise 'if' number is NOT numeric, print this
    
#Other built-in string methods; not all inclusive
islower() #This verifies if the string ONLY contains lowercase characters
isspace() #This verifies if the string ONLY contains white spaces 