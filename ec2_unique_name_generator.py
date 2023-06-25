import random #the 'import' keyword is used to make code in one module availabile in another. The 'random' keyword generates random numbers
import string #the 'import' keyword is used to make code in one module availabile in another. The 'string' keyword generates a collection of alphabets, words or characters

def generate_EC2_names(user_EC2_instances, user_department): #the 'def' keyword' is used to define/create.
    unique_names = [ ]
    for i in range(user_EC2_instances): #The 'range' keyword generates a collection/sequence of numbers starting w/0; it can be used to index in collections, such as a string
        generated_name = user_department + '-'
        for j in range(10): #The 'in' operator checks whether a specified value is present in a sequence (i.e. 'range')
            generated_name += random.choice(string.ascii_letters + string.digits) #'choice' returns a randomly selected element from a specified sequence; 'ascii_letters' contains all the English letters from a-z; 'digits' are numeric data types
        unique_names.append(generated_name)
    return unique_names #The 'return' keyword can be used inside a function to send a function's result back to the caller

user_EC2_instances = int(input('Please enter the number of instances you want names for: '))
print('You entered', user_EC2_instances, 'EC2 instances.\n')
    
user_department = str(input('Please enter your department: '))
print('You entered', user_department, 'as your department.\n')

print('Your EC2 names are as follows: \n')

unique_names = generate_EC2_names(user_EC2_instances, user_department)
for generated_name in unique_names:
    print(generated_name)
