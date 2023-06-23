# The bit operators are: &, |, ~, ^, <<, >>
first_bit = 1
second_bit = 0

# You will only see 1 when both of the bits are 1, otherwise you will just get 0
#print(first_bit & second_bit)

# You will only see 1 if one of the bits is 1
#print(first_bit | second_bit)

# When one of the numbers is 0 than the result is 1; when both are 0, the result is 0
#print(first_bit ^ second_bit)

# If placed in fron of 1, you'll get -2; if placed in front of 0, you'll get -1
#print(~1)
#print(~0)

# Both left and right shift operators are left-shift operator,” typically used on long sequences of bits
# Left-shift operator works by multiplying your decimal number by 2 to a certain power; multiply the number by 2
#print(12 << 1) #Shifted by 1 bit; multiply the number by 2
#print(12 << 2) #Shifted by 2 bits; multiply the nuber by 4
#print(12 << 3) #Shifted by 3 bits; multiply the number by 8

# Right-shift operator works by dividing your decimal number by 2 to a certain power; divide the number by 2
print(12 >> 1) #Original value divided by 2; divide the number by 2
print(12 >> 2) #Original value divided by 4; divide the number by 4
print(12 >> 3) #Original value divided by 8; divide the number by 8