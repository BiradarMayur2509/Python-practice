"""
*                     *
* *                 * *
*   *             *   *
*     *         *     *
*       *     *       *
*         * *         *
*         * *         *
*       *     *       *
*     *         *     *
*   *             *   *
* *                 * *
*                     *

"""

N = int(input())

for i in range(1,N+1):
    if i == 1:
        spaces = (2*(N-i)) *" "
        row = "* " + (2*spaces) + "* "
    else:
        spaces = (2*(N-i)) *" "
        hollow_spaces = (2 * i -4) *" "
        left_pyramid = "* " + hollow_spaces +"* " + spaces 
        right_pyramid = spaces + "* " + hollow_spaces +"* "
        row = left_pyramid + right_pyramid
    print(row)
    
for i in range(N,0,-1):
    if i == 1:
        spaces = (2*(N-i)) *" "
        row = "* " + (2*spaces) + "* "
    else:
        spaces = (2*(N-i)) *" "
        hollow_spaces = (2 * i -4) *" "
        left_pyramid = "* " + hollow_spaces +"* " + spaces 
        right_pyramid = spaces + "* " + hollow_spaces +"* "
        row = left_pyramid + right_pyramid
    print(row)