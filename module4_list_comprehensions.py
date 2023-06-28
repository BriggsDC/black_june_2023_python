#This is ideal for really long list (i.e. 1-100)
#numbers = [ ] #Here you created an empty list
#for i in range(1, 101): #Next inside a 'for' loop you appended numbers to it
    #numbers.append(i)
#print(numbers)

#The above method takes up a lot of space; the alternative way below is special to Python and a shortcut
#numbers = [ i for i in range(1, 101)] #Its alnost s if you moved the loop into the square brackets w/ the control variable name 'i' in front of the loop, otherwise you'll get an error'
#print(numbers)

#The method below skips numbers that are divisible by 3
numbers = [ i for i in range(1, 101) if i % 3 != 0] #Uses the modula division of 3 if different from 0
print(numbers) #A 'list comprehension' is an actual list that is created on the fly when you run your Python program; its mot necessary in programming, but it is a nice shortcut.




