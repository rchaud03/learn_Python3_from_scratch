"""
Importing and using modules to reduce the amount of coding done
https://docs.python.org/3/library/
"""
import math
#Importing the math module when you only need the square root out of it uses additional resources.
from math import sqrt
#instead we import just the square root module out of the math module
class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))


m = ModulesDemo()
m.builtin_modules()