# baisic hello workd program
print("hello world")



# imports example
import sys
print(sys.version)
# for checking python keywords
import keyword
print(keyword.kwlist)
# importing operator module
import operator
print(operator.add(2, 3))  # example of using operator module
print(operator.mul(2, 3))  # example of using operator module
print(operator.sub(2, 3))  # example of using operator module  \# subtraction
print(operator.truediv(2, 3))  # example of using operator module \# division
print(operator.floordiv(2, 3))  # example of using operator module \# floor division
print(operator.mod(2, 3))  # example of using operator module \# modulus
print(operator.pow(2, 3))  # example of using operator module \# power
# end of operator module examples
# import date and time and try some examples
from datetime import datetime
now = datetime.now()
print("Current date and time: ", now)
print("Current year: ", now.year)
print("Current month: ", now.month)
print("Current day: ", now.day)
print("Current hour: ", now.hour)
print("Current minute: ", now.minute)
print("Current second: ", now.second)
print("Current microsecond: ", now.microsecond)
print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current date and time: ", now.strftime("%A, %B %d, %Y"))
print("Current date and time: ", now.strftime("%I:%M %p"))
# end of datetime module examples
import os
print(os.name)  # example of using os module
print(os.getcwd())  # example of using os module
print(os.listdir())  # example of using os module
# end of os module examples