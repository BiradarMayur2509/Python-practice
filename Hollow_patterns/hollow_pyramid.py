"""
   *
  * *
 *   *
* * * *

"""

N = int(input())

for i in range(1,N+1):
    if i == 1:
        spaces =(N - 1) * " "
        row = spaces + "* " + spaces 
    elif i == N:
        row = "* " * N 
    else :
        left_spaces = (N - i) * " "
        hollo_spaces = (2* i - 4) * " "
        row = left_spaces + "* " + hollo_spaces + "* "
    print(row)