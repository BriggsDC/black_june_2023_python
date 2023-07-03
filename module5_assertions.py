#You’d use “assertions” to raise exceptions by yourself. Assertions are assumptions in your program that should always be True.
def calculate_inverse(number):
    assert (number !=0), 'Got 0 as number!' #Note the new key word, 'assert.' This is a condition you'd assume would always be true for this specific function to work correctly. If tru Python simply moves to the next line.If the condition is NOT true, Python shows the error message listed after the comma
    return 1/number

calculate_inverse(0) #Geberally, "assertions” are used for debugging/testing and documenting your code.