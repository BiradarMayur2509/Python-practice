"""
*                     * 
* *                 * * 
* * *             * * * 
* * * *         * * * * 
* * * * *     * * * * * 
* * * * * * * * * * * *
"""

N = int(input())

for i in range(1,N+1):
    left_star = i * "* "
    middle_space = 4 * (N-i) * " "
    right_star = i * "* "
    print(left_star + middle_space + right_star)