import sys
import keyword
import operator
from datetime import datetime
import os

print("Hello, World!")  # Basic Hello World Program
print(keyword.kwlist) # List all Python Keywords


len(keyword.kwlist) # Python contains 35 keywords


# identifier examples
# print(keyword.kwlist[35]) # IndexError: list index out of range
# 1var = 10 # Identifier can't start with a digit
# val2@ = 35 # Identifier can't use special symbols
# import = 125 # Keywords can't be used as identifiers


# Single line comment
val1 = 10  # This is a single line comment

"""
This is a multi-line comment
using triple double quotes
""" 

'''This is a multi-line comment
using triple single quotes'''

p1 =  10+2
print(p1) # Addition
p2 = 10-2
print(p2) # Subtraction
p3 = 10*2
print(p3) # Multiplication
p4 = 10/2
print(p4) # Division
p5 = 10%2
print(p5) # Modulus
p6 = 10//2
print(p6) # Floor Division
p7 = 10**2
print(p7) # Exponentiation  # 10^2 = 10*10 = 100


# indentation example for the if-else statement
p = 10
if p == 10:
    print ('P is equal to 10') # correct indentation
    if p < 15:
        print('P is less than 15') # correct indentation
        if p < 12:
            print('P is less than 12') # correct indentation
            if p < 11:
                print('P is less than 11') # correct indentation
            else:
                print('P is not less than 11') # correct indentation
        else:
            print('P is not less than 12') # correct indentation
    else:
        print('P is not less than 15') # correct indentation
else:
    print('P is not equal to 10') # correct indentation     
    
    
    
# using operator module for arithmetic operations
print(operator.add(10, 2))  # Addition
print(operator.sub(10, 2))  # Subtraction
print(operator.mul(10, 2))  # Multiplication
print(operator.truediv(10, 2))  # Division
print(operator.mod(10, 2))  # Modulus
print(operator.floordiv(10, 2))  # Floor Division
print(operator.pow(10, 2))  # Exponentiation  # 10^2 = 10*10 = 100


