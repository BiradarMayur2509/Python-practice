"""
write a program to print number from 1 to N each row forming a
ractanglular pattern of M rows and N columns 

o/p

1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 
"""

M = int(input())
N = int(input())

for i in range(1,M+1):
    for j in range(1,N+1):
        print(j,end=" ")
    print()
