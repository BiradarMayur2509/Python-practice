"""
* 
* * 
*   * 
*     * 
* * * * * 
"""

N = int(input())

for i in range(1,N+1):
    if (i == 1):
        spaces = 2*(N-i) *" "
        row = "* " + spaces
    elif (i == N):
        row = "* " * N 
    else:
        right_spaces = (2 * (N - i))* " "
        hollow_spaces = (2 * i - 4) * " "
        row = "* " + hollow_spaces + "* " + right_spaces
    print(row)