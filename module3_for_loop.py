#for letter in 'hello!': #The word 'letter' is the control variable Theword 'in' is also a keyword that introduces the range of possible values of the sequence you're scanning'
    #print('Current letter:', letter)

#for counter in range(1, 11): #The range function generates the desired integer values for a controlled variable; 1 is the start value and 11 is the stop value; the start value is inclusive in the sequence, but the stop value is exclusive
    #print(counter)
#print('Finished!')

#The range function has 3 versions
#for counter in range(11): # Here the default value of 0 will be used; result will output 0-10
    #print(counter)
#print('Finished!')

for counter in range(1, 11, 2): # Here the last argument (2) is the increase amount; this will generate every second number (or all odd numbers)
  print(counter)
print('Finished!')
