"""
* * * * * * * * 
* 0 0 0 0 0 0 * 
* 0 0 0 0 0 0 * 
* * * * * * * * 

"""
M = int(input())
N = int(input())
for i in range(1,M+1):
    if (i == 1 or i == M):
        row = "* " * N
    else:
        zeros = "0 " * (N - 2)
        row = "* " + zeros + "* "
    print(row)