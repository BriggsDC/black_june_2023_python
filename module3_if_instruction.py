user_age = int(input('What is your age? '))
if user_age > 30: #User is older than 30
    print('You are over 30 years old') # Both of these print invocations form a so-called "block"
    print('Sorry, you do not qualify') # Remember  instructions from the same 'If block' MUST have the same indentation
    
elif user_age == 30: #User is exactly 30
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
    
else: #User is 30 or younger
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')