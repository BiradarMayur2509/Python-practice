"""
*                                 *
* *                             * *
*   *                         *   *
*     *                     *     *
*       *                 *       *
*         *             *         *
*           *         *           *
*             *     *             *
* * * * * * * * * * * * * * * * * *

"""

N = int(input())

for i in range(1,N+1):
    if i == 1:
        spaces = 2*(N-i) * " "
        row = "* " + (spaces * 2) + "* "
    elif i == N:
        row = 2*("* " * N)
    else:
        right_spaces = (2*(N-i))*" "
        left_spaces = (2*(N-i))*" "
        hollow_spaces = (2*i-4) * " "
        left_tri = "* " + hollow_spaces + "* " + right_spaces
        right_tri = left_spaces + "* " + hollow_spaces + "* "
        row = left_tri + right_tri
    print(row)
        