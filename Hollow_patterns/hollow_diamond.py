"""
      *       
     * *
    *   *
   *     *
  *       *
 *         *
*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *

"""


N = int(input())

for i in range(1,N+1):
    if i == 1 :
        spaces = (N - i) *  " "
        row = spaces + "* " + spaces
    else:
        left_spaces = (N - i ) * " "
        hollw_spaces = (2 * i - 4) * " "
        row = left_spaces + "* " + hollw_spaces + "* "
    print(row)
    
for i in range(N-1,0,-1):
    if i == 1 :
        spaces = (N - i) *  " "
        row = spaces + "* " + spaces
    else:
        left_spaces = (N - i ) * " "
        hollw_spaces = (2 * i - 4) * " "
        row = left_spaces + "* " + hollw_spaces + "* "
    print(row)