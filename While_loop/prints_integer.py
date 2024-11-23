# Given two integer numbers M and N, write programme to print the M and N.
# use while loop to solve this problem.
# Input: M = 5, N = 10
# Output: 5 6 7 8 9 10

M = int(input())
N = int(input())
count = M

while count <= N:
    print(count)
    count +=1