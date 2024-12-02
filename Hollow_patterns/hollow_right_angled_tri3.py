"""

      *
    * *
  *   *
* * * *

"""

N = int(input())

for i in range(1,N+1):
    if (i == N):
        row = "* " * N
    elif (i == 1):
        left_spaces =  (2*(N - i)) * " "
        row = left_spaces + "* "
    else:
        left_spaces = (2* (N - i)) * " "
        hollow_spaces = (2* i - 4) * " "
        row = left_spaces + "* " + hollow_spaces + "* "
    print(row)