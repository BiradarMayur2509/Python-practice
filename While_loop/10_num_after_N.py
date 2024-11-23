# Write a program that reads number N and print 10 number after N.
# input N = 5
# use while loop to solve this problem.
"""
output
6
7
8
9
10
11
12
13
14
15 
"""

N = int(input("Enter your number: "))
count = 1

while count <= 10:
    N = N + 1
    print(N)
    count = count + 1