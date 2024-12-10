"""
+ - - - - - +
|           |
|           |
|           |
|           |
|           |
+ - - - - - +

"""

N = int(input())

for i in range(0,N+2):
    if i == 0 or i == N+1 :
        row = "+ " + ("- " * N) + "+" 
    else:
        spaces = N * "  "
        row = "| " + spaces + "|"
        
    print(row)