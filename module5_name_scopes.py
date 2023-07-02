
#def show_truth():
    #mysterious_var = 'New Surprise!'
    #print(mysterious_var)
    
#show_truth()
 
#You can also define the variable outside the function defintion before the function call
#def show_truth():
    #print(mysterious_var)
    
#mysterious_var = 'New Surprise!' #variables that exist otside the function have a scope inside the function's body; this means functions can see them and use them
    
#show_truth()
 
#Below is called 'shadowing.' 
#def show_truth():
    #mysterious_var = 'New Surprise!' #'mysterious_var' is 2 different variables w/ 2 different values. Shadowing is when the local variable inside a function shadows the global variable.
    #print(mysterious_var)
    
#mysterious_var = 'Surprise!' #'mysterious_var' is 2 different variables w/ 2 different values. Shadowing is when the local variable inside a function shadows the global variable.
#print(mysterious_var)
#show_truth()
#print(mysterious_var)
 
#If you want to modify a global variable w/in function
#def show_truth():
    #global mysterious_var #Note the new 'global' key word; this is an added new function. This means do NOT use shadowing for the function 'mysterious_var' AKA, don't create a temp variable, instead use the global variable
    #mysterious_var = 'New Surprise!'
    #print(mysterious_var)
    
    #mysterious_var = 'Surprise!'
    #print(mysterious_var)\
    #show_truth()
    #print(mysterious_var)
 
#Be careful when creating lists
#def show_truth():
    #mysterious_var = ['New Surprise!'] #New list w/ a single element
    #print(mysterious_var)
    
#mysterious_var = ['Surprise!']
#print(mysterious_var)
#show_truth()
#print(mysterious_var)
 
#If you assign a new list to the same variable in a function, shadowing works fine. BUT, if you change the list using a method, using square brackets or the ‘del’ instruction, the list OUTSIDE the function will reflect the change. 
def show_truth():
    mysterious_var.append('New Surprise!')
    print(mysterious_var)
   
mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)
 
 
 
 
 
   