"""
        # 
      + # 
    + + # 
  + + + # 
+ + + + # 
  + + + # 
    + + # 
      + # 
        # 
"""

N = int(input())

for i in range (1,N+1):
        spaces = " " *  (2*(N - i) )
        pluses = "+ " * (i - 1)
        print(spaces + pluses + "# ")
        
for i in range(N - 1, 0 ,-1):
    spaces = " " *  (2*(N - i) )
    pluses = "+ " * (i - 1)
    print(spaces + pluses + "# ")