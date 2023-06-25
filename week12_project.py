import random
import string

def generate_EC2_names(user_EC2_instances, user_department):
    names = [ ]
    for i in range(user_EC2_instances):
        name = user_department + '-'
        for j in range(10):
            name += random.choice(string.ascii_letters + string.digits)
        names.append(name)
    return names

user_EC2_instances = int(input('Please enter the number of instances you want names for: '))
print('You entered', user_EC2_instances, 'EC2 instances.\n')
    
user_department = str(input('Please enter your department: '))
print('You entered', user_department, 'as your department.\n')

print('Your EC2 names are as follows: \n')

names = generate_EC2_names(user_EC2_instances, user_department)
for name in names:
    print(name)