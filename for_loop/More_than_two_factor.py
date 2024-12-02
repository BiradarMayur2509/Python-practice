"""
Given a number N, write a program to find counte of factors of N.
Print "Number has more than 2 factors" if count of factor is greater than 2 
otherwise print "Number doesn't have more than 2 factors".
"""

N = int(input())
count = 0
for i in range(1,N+1):
    if N % i == 0:
        count +=1
    
if count > 2:
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors ")
