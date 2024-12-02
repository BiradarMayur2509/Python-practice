"""
________
|      /       
|     /      
|    /     
|   /    
|  /   
| /  
|/

"""
N = int(input())

for i in range(N+1,0,-1):
    if (i == 1):
        row = "|/"
    elif (i == N+1):
        row = "_" * (N+1)
    else:
        hollow_spaces = " " *(i -2)
        right_spaces = (i-1) * " "
        row = "| " + hollow_spaces + "/ " + right_spaces
    print(row)
