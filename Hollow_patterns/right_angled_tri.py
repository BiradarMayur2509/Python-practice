"""
. 
. .
. 0 .
. 0 0 .
. 0 0 0 .
. 0 0 0 0 .
. . . . . . .

"""

N = int(input())

for i in range(1,N+1):
    if (i == 1):
        row = ". " 
    elif (i == N):
        row = ". " * N
    else:
        right_space = (2*(N - i) * " ")
        zeros = "0 " * (i - 2)
        row = ". " + zeros + ". " + right_space
    print(row)