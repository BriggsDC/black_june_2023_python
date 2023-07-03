#Factorials
#3! = 1*2*3 = 6
#5% 1*2*3*4*5 = 120

#1! = 1
#2! = 1 * 2
#3! = 1 * 2 * 3
#4! = 1 * 2 * 3 * 4
#5! = 1 * 2 * 3 * 4 * 5

#Iterative
def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1): #This called 'iterative' because inside the function you used a'for' loop to iterate the sequence of numbers
        factorial *= x
    return factorial

print(get_factorial(6))

#Recursive/Recursion
def get_factorial_recursive(number):
    if number <= 1: #This provides a stop function; otherwise function runs to infinity and crashes when you run out of memory.
        return 1
    return number * get_factorial_recursive(number - 1) #Here the function calls itself
