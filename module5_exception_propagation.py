#In Python, exceptions are propagated through functions. This is ideal for multiple functions that call each other.
#This program collects user info about their birthday
def get_day(user_info):
    day = int(input('What is the day of your birthday? '))
    user_info.append(day)
    
def get_month(user_info):
    month = int(input('What is the month (1-12) of your birthday? '))
    user_info.append(month)  
    
def get_year(user_info):
    year = int(input('What is the year of your birthday? '))
    user_info.append(year)
    
def get_user_bday(user_info):
    try: #Here you can insert a single try/except statement that applies to all functions
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print('So your birthday is', user_info)
    except ValueError:
        print('Sorry, but you entered incorrect data')
        
print('Hi, I will collect some info about your birthday!') 
user_info = [ ]
get_user_bday(user_info)
    
    
    
    
    
    