"""
Given a starting number, S and N 
,write a programme that brings a 
square of N Rows and N column using numbers 
starting from s.

i/p : 3 and 4
o/p :
3 4 5 6 
3 4 5 6 
3 4 5 6 
3 4 5 6 

"""

S = int(input())
N = int(input())


for i in range(1,N+1):
    for j in range(S,N+S):
        print(j,end =" ")
    print()