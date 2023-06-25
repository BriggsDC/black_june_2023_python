#'Break' keyword
#while True: # Has a condition that is always True
    #name = input('Enter your name or EXIT to close the program: ')
    #if (name == 'EXIT'):
        #break #This makes it possible to escape the loop
    #print('Hello', name)

#'Continue' keyword
for i in range(1, 21):
       if i % 5 == 0: #Modular division is used here. If a number modular divided by 5 is. 0, it means the number is divisible by 5
           continue #This function won't count the number divisible by 5; the whole loop isn't exited, it just moves on to the next value
       print(i)