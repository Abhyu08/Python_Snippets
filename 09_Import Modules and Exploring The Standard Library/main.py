import math
#Here instead of math we can specify user specific module.

import math as m
from math import floor
from math import floor as flr

import os
import sys
sys.path.append("/Users/something/Custum_modulePath/")

def print_hi(name):

    #same
    print(math.pi)
    print(m.pi)

    #only imported floor() function instead of whole module here...
    print(floor(3.14))
    print(flr(3.14))

    #we can manullay add path of custom module in program itself..
    print(sys.path)

    #we can set PYTHONPATH permanently through environment variables.

    #DUNDER implies __nameOfkeyword__
    print( 'File Path => ', os.__file__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
