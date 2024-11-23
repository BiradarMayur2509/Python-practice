# use while loop to solve this problem.
# Given two integers M and N, write program to print a solid rectangle pattern of M rows and N columns using (*) character.
# input : M = 5, N = 4
# output :  * * * 
#           * * * 


M = int(input())
N = int(input())
count = 1

while count <= M:
    print("* " * N)
    count += 1