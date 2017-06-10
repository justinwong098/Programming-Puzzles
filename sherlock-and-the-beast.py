#!/bin/python3

import sys
import math


t = int(input().strip())
listN0 = []
for a0 in range(t):
    n = int(input().strip())
    listN0.append(n)
    
# N == 3x + 5y
# where x == number of sets of 5's
# where y == number of sets of 3's

def solveDecentNumber(listN):
    for n in listN:
        y = 0
        x = int(n/3)
        z = n % 3
        if z == 0:
            y = 0        
        else:
            while z % 5 != 0:
                if x < 0:
                    break                                        
                x -= 1
                z += 3
            y = int(z / 5)
            

        if x >= 0:            
            print("5"*3*x + "3"*5*y)    
        else:
            print(-1)

solveDecentNumber(listN0)
