#In Python you can use an ‘if statement’ inside another ‘if statement.’ AKA, a nested if statement.
#answer_a = input('Do you like traveling? y/n: ')
#if answer_a == 'y':
    #print('Good!')
#else:
    #print('Sorry to hear that')
   
  
 #Indentation is VERY important! (Especially multi-level indentation)
#answer_a = input('Do you like traveling? y/n: ')
#if answer_a == 'y': #indented w/ 4 spaces
   #answer_b = input('And do you like Asia? ')
   #if answer_b == 'y': #indented w/ 8 spaces
   #else: #indented w/ 8 spaces
      #print('Excellent! You can win a ticket to Thailand!')
#else: #indented w/ 4 spaces
    #print('Sorry to hear that')
    

#My version    
purchase_days = int(input('How many days ago have you purchased this item? '))
item_use = input('Have you used the item at all [y/n]? ')
item_status = input('Has the item broken down on its own [y/n]? ')
if purchase_days < 10: 
   item_use == 'y'
   print('You can get a refund.')
else:
   print('You cannot get a refund.')
   
#Lab recommended version
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')
       
