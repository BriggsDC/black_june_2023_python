#Dictionaries are collections used to store key value pairs.
#emails = { #This particular dictionary has 3 entries consisting of a person's name and e-mail address; similar to a phonebook
    #'Anne Stahl': 'astahl@gmail.com',
    #'Peter Small': 'peters@yandex.com',
    #'Mark Steel': 'mark@steel.com'
#}

#To write out a message and find out Mark's email...
#print(emails['Mark Steel']) #This means, show me the value of Mark Steel; show me the e-mail address
#In lists and tuples you access individual elements by providing the index w/in a square bracket. In dictionaries, you access specific values by providing the key w/in the same square brackets

#A langauage dictionary example...
#spanish_animals = { #Dictionaries are created using curly brackets { }. Inside the brackets is where you provide key value pairs. First is the “key” a colon and then some value for the key.
    #'dog': 'el perro',
    #'cat': 'el gato',
    #'horse': 'el caballo',
    #'bird': 'el pájaro'
    #}
#print(spanish_animals ['bird']) #This looks up the spanish translation of 'bird'

#Dictionary keys don’t have to be strings, they can be of any other immutable data type (i.e. integers, floats or tuples as keys). A list cant become a key, but it can become a value.
#While the key must be immutable, the value data can be of any data type available in Python.
city_ratings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanoi': [7, 6, 4, 5],
    'Manila': [6, 6, 4, 4, 5]
    }