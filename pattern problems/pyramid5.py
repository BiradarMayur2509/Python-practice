"""
   * 
  * * 
 * * * 
* * * *
"""

N = int(input())

for i in range(1,N+1):
    spaces = (((N - i)) * " ")
    star = i * "* "
    print(spaces + star)