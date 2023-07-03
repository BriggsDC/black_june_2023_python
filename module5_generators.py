def get_number():
    for i in range(1, 4): #You can use the 'next' generator to get numbers up to 4 exclusively
        yield i #'i' is the control variable. Whenever you use the key word 'yield' instead of 'return' your function becomes a generator

#Generators generate certain values one by one
generator = get_number() #In order to use, you must store a generator inside a variable
print(next(generator)) #Here 'next' is the function and 'generator' is it's argument
print(next(generator))
print(next(generator))

#You can also use a 'for' loop w/ a generator
for x in get_number():
    print(x)

#You can turn generators into lists using the list function
numbers = list(get_number())
print(numbers)




