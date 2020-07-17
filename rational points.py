import math
from legendre01 import util
from legendre01.util import *
#Imported Bessers Program for Legendre's

def solver(p,equation):
    n=0
    for x in range (0,p):
        q=(x**(3)+equation[0]*x+equation[1])

        if q==0:
            n+=1
            print(x,q)
        elif legendreSymbol(q,p)==1:
            n+=2


    return n
# calculates the values of equation for 1 through p-1 and calls Legendre to check if it is a quadratic residue
# adds one solution if equal to zero, 2 if it quadratic residue
