#'Pass' is an additional loop feature you can use as a placeholder so your code wont throw errors
#for i in range (11):
    #pass

#Nested loop
#for a in range(1,6):
    #for b in range(1, 6):
        #print(a, 'x', b, '=', a * b)
   
#'Else' is an additional loop feature that is rarely used. However, when used it is the claues after a 'for' and 'while' body   
i = 2
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)