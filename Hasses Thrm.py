import math
from RationalRoots01 import util
from RationalRoots01.util import *
#Made rational roots program into a package, imported it

eq=[1,3]
def accuracy(p):
    num=solver(p,eq)
    points=abs(num-p+1)
    bound=2*(math.sqrt(p))
    string=("Points: ", points, " Bound: ", bound, " Difference is ", points-bound)
    return string
# Calculate both values for Hasse's Thrm and return

print(accuracy(3))
print(accuracy(7))
print(accuracy(13))
print(accuracy(19))
print(accuracy(23))
#prints the results over a series of different finite fields
