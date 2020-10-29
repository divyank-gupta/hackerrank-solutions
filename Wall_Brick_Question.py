# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:50:26 2019

@author: DIV
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY wallPositions
#  2. INTEGER_ARRAY wallHeights
#

def maxHeight(wallPositions, wallHeights):
    # Write your code here
    mx1 = 0
    for i in range(0,len(wallPositions)-1):
        #if wallPositions[i]<(wallPositions[i+1]-1):
        gap = wallPositions[i+1]-wallPositions[i] - 1
        hdiff = abs(wallHeights[i+1]-wallHeights[i])
        mx=0
        if  gap>hdiff:
            print("gap is greater")
            low = max(wallHeights[i+1],wallHeights[i])+1
            remgap = gap - hdiff -1
            mx = low+remgap//2
        else:
            print("height is greater or equal")
            mx = min(wallHeights[i+1],wallHeights[i])+gap
        mx1 = max(mx1,mx)
    return mx1

print(maxHeight([1,10],[3,4]))