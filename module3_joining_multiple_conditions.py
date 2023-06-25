# Boolean operators are used to execute code when 2 or more conditions are met at the same time OR, when executing code when at least 1 of many conditions is met.
# There are 3 Boolean Operators in Python: And, Or, Not

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange programme') #Executes ONLY if both conditions are met
else:
    print('Sorry, you do not qualify')
  
  
user_country = input('What is your country?')
if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange programme')
else:
    print('Sorry, you do not qualify')
  
  
user_country = input('Where do you come from? ')
if not user_country == 'Germany':
    print('you are not from Germany!')
else:
    print('you are from Germany')
    
    
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if not user_country == 'Germany' and user_age < 25 or user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('You don\'t qualify!')
    
# Boolean operators have their priorities: Not, And then Or. Using brackets is not mandatory, but it improves readability.

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')
if ((not user_country == 'Germany') and user_age < 25) or  (user_country == 'Germany' and user_age < 23):
    print('You qualify!')
else:
    print('You don\'t qualify!')