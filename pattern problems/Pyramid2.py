'''
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 

'''


N = int(input())

for i in range(1,N+1):
    spaces = (N - i)
    number = (str(i) + " " ) * (i)
    print(" " * spaces + (number))