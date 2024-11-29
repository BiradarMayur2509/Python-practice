'''
      *
    * *
  * * *
* * * *
'''

N = int(input())

for i in range(1,N+1):
    spaces = 2*(N-i)
    star = i 
    row = (spaces * " " + star * "* ")
    print(row)