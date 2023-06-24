#counter = 1
#while counter < 11:
    #print(counter) #This is the beginning of the body of the 'loop'
    #counter += 1 #This means increase the counter by 1; this is so comman it has a name, 'incrementation.' Remember to align w/ 'print' block to avoid inifinite loop errors.
#print('Finished!') #This should be aligned w/ opening 'while' loop


#secret_number = 14
#user_input = int(input('Try to guess the secret number from 0 to 20: '))
#while user_input != secret_number: #NOT equal to secret_number
    #print('Wrong!')
    #user_input = int(input('Try to guess the secret number from 0 to 20: '))
#print('Perfect! You have guessed the secret number.')


secret_number = 14
print('''
    ==========================
    === SECRET NUMBER GAME ===
    ==========================
    ''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number: #NOT equal to secret_number
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')