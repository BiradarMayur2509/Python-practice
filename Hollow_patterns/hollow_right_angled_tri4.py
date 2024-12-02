"""
* * * * *
  *     *
    *   *
      * *
        *
"""

N = int(input())

for i in range(N,0,-1):
    if i == 1:
        left_spaces = " " * (2*(N-1))
        row =  left_spaces + "* "
    elif i == N :
        row = ("* ") * N 
    else:
        left_spaces = (2* (N-i)) * " "
        hollow_spaces = (2 * i - 4) * " "
        row =  left_spaces +"* " + hollow_spaces + "* "
    print(row)
