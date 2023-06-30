#input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]
#sum = 0.0
#for number in input_numbers:
    #sum += number
#average = sum / len(input_numbers)
#print(average)

#This turns the above code into a function
#input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

#def get_average (input_numbers): #What is encapsulatedin () is a parameter
    #sum = 0.0
    #for number in input_numbers:
        #sum += number
    #average = sum / len(input_numbers)
    #print(average)
    
#get_average([5.0, 3.5, 7.8, 9.9, 10.0]) #Here the list is an argument; the value of the argument is assigned to the parameter named 'input_numbers'

#You can define functions w/ more than 1 parameter.
def print_letter_count(text, letter): #This function has 2 parameters seperated by a comma; it takes a string and a letter counting how many times the number appears in the string
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter) #When invoking a function somewhere in your code, be sure to provide both of them

#This counts how many times the letter 'e' appears in the string
#print_letter_count('Welcome', 'e')

#Here's a more complicated example
#print_letter_count('People say nothing is impossible, but I do nothing every day.', 'a') #Note the order of an argument is important; it should be text or string THEN the letter. Be sure note to confuse the order.

#Named arguments AKA key word arguments
print_letter_count(text='Welcome', letter='e') 

print_letter_count(letter='e', text='Welcome') #With named arguments, you can swap the places and the functions will still be correct; letter comes first here and text second but the function still works


