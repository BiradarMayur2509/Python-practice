'''
****
 ***
  **
   *
'''

N = int(input())

for i in range(N,0,-1):
    spaces = (N - i) * " " 
    stars = i * "*" 
    print(spaces + stars)  # print the spaces and stars together
    