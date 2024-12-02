"""
          1
        2 2
      3   3
    4     4
  5       5
6         6
  5       5
    4     4
      3   3
        2 2
          1

"""

N = int(input())

for i in range(1,N+1):
    if i == 1:
        left_spaces = (2*(N - i)) * " "
        row = left_spaces + (str(i) + " ")
    else:
        left_spaces = (2*(N - i)) * " "
        hollow_spaces = (2* i - 4) * " "
        num = str(i) + " "
        row = left_spaces + num + hollow_spaces + num 
    print(row)

for i in range(N-1,0,-1):
    if i == 1:
        left_spaces = (2*(N - i)) * " "
        row = left_spaces + (str(i) + " ")
    else:
        left_spaces = (2*(N - i)) * " "
        hollow_spaces = (2* i - 4) * " "
        num = str(i) + " "
        row = left_spaces + num + hollow_spaces + num 
    print(row)
    
        
        