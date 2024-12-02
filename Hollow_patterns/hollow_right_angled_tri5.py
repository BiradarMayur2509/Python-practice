"""
# # # # # #
+       +
+     +
+   +
+ +
+

"""

N = int(input())

for i in range(N,0,-1):
    if i == N :
        row = "# " * N 
    elif  i == 1:
        spaces = (2 * (N-1)) * " "
        row = "+ " + spaces 
    else:
        hollow_spaces = (2 * i - 4) * " "
        right_spaces = (2 * (N - i)) * " "
        row = "+ " + hollow_spaces + "+ " + right_spaces
    print(row)