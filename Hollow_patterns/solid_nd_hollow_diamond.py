"""
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 *       *
  *     *
   *   *
    * *
     *

"""

N = int(input())

for i in range(1,N+1):
    spaces = (N-i) * " "
    star = "* " * i
    print(spaces + star)

for i in range(N-1,0,-1):
    if i == 1:
        spaces = (N-i) * " "
        row = spaces + "* " + spaces
    elif i == N:
        row = "* " * N 
    else:
        left_spaces = (N-i) * " "
        hollow_spaces = (2 * i - 4) * " "
        row = left_spaces + "* " + hollow_spaces + "* "
    print(row)
