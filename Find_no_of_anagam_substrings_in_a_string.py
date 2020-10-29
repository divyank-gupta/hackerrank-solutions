# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 00:12:49 2020

@author: DIV
"""

#find all possible substrings

s = "xyyx"
l = []
##l = s.split()
#
#counter = li = len(s)
#count = 0
#li = 0
#while li < counter:
#    for i in range(0,counter):
##        print(s[i])
##        print(i+li)
#        if i + li >= counter:
#            break
#        print(s[i:i+li+1])
#        s1 = s[i:i+li+1]
#        s2 = sorted(s1)
#        if s2 in l:
#            count = count + 1
#        else:
#            l.append(s2)
#    li = li + 1
#print(l)
#print(count)
count = 0
for i in range(len(s)):
#    print("Loop:",i+1)
    for j in range(len(s)):
#        print(j,":",+i+j+1)
        if i+j+1 <= len(s):
            print(s[j:i+j+1])
            s1 = sorted(s[j:i+j+1])
            s2 = ('').join(s1)
            print('s2:   '+s2)
            if s2 in l:
                count = count + 1
            l.append(s2)
print(count)
print(l)
