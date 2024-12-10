"""
* 
* * * 
* * * * * 

"""

N = int(input())
count = 1
for i in range(0,N):
    if i == 0:
        row = "* " 
    else:
        count += 2 
        row = "* " * count 
    print(row)