# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:40:29 2019

@author: DIV
"""

n = 5
y = 1 + (n-1)*2

print("Pattern 1")
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end="")
    print("\n")
    
print("Pattern 2")
for i in range(1,n+1):
    for j in range(0,n+1-i):
        print("*",end="")
    print("\n")

print("Pattern 3")
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,1+(i-1)*2+1):
        print("*",end="")
    print("\n")

print("Pattern 4")
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print("\n")
    
print("pattern 5")
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(0,n-i+1):
        print("*",end="")
    print("\n")
    
print("pattern 6")
number_of_stars = 8
num = number_of_stars
counter = 0
for i in range(1,num):
#    if num - i>0:
#        num -= i
#        counter += 1
##    elif num - i == 0:
##        counter += 1
##        break
#    else:
#        counter +=1
#        break
    num -= i
    counter += 1
    if num<=0:
        break
        
print("Number of lines are:" ,counter)
print("NUmber of stars to be printed:",number_of_stars)
c=0
for i in range(1,counter+1):
    for j in range(1,counter-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("* ",end="")
        c+=1
        if c>=number_of_stars:
            break
#        print(c,end="")

    print("\n")