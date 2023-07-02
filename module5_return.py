#Return a meaningful value from a function
#def get_average(input_numbers):
    #sum = 0.0
    #for number in input_numbers:
        #sum += number
    #average = sum / len(input_numbers)
    #return average #'Return' is a key wor value that returns a meaningful value. Note that no brackets are used because 'return' is not a function. It doesn't print the average or cause any effect, it instead just returns a 'meaningful value'

#Here you changed the code from being ignored, printing it to the output
#print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

#Save the return value in a variable and then later use it in the code somehow
#average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
#if average > 5.0:
    #print('The average is too high!')
   

#The 'return' keyword function that does 2 at the same time. It gives the result and it also immediately exits a function. This means that any instruction after the ‘return’ statement will be ignored.
#def get_average(input_numbers):
    #sum = 0.0
    #for number in input_numbers:
        #sum += number
    #average = sum / len(input_numbers)
    #return average
    #print('Show me!')

#get_average([2])

#This function checks whether the first and last elements of a list are equal 
def is_first_last_equal(number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_last_equal([10, 20, 30, 40, 10])) #Should print True

print(is_first_last_equal([10, 20, 30, 40, 50])) #Should print False

#Another option
def is_first_last_equal(number_list):
    if len(number_list) == 0: #Here at the beginning of the function youre checking if the file size of the function is 0 (i.e. the list doesn't have any elements), you use the 'return' keyword to immediately exit the function
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
        
print(is_first_last_equal([])) #SHould print None