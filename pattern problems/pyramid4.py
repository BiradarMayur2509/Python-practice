"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

"""

N = int(input())

for i in range(1,N+1):
    str_i = str(i)
    print((str(str_i) + " ") * i)
    
for i in range(N-1,0,-1):
    str_i = str(i)
    print((str(str_i) + " ") * i)