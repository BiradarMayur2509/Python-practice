'''
   *
  **
 ***
####
'''

N = int(input())

for i in range(1,N+1):
    spaces = (N-i)
    star = i 
    
    if i < N:
        print(' ' * spaces + '*' * star)
    else:
        print(' ' * spaces + '#' * star)  # This line is not necessary, but
