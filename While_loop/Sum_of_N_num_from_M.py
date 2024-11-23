# use while loop to solve this problem.
# Write a program that reads to numbers M and N and print the sum of N numbers from M.

# Sample Input : 7 3
# calculation : 7 + 8 + 9 = 24
# Sample Output : 24

M = int(input())
N = int(input())
total_sum = 0
count =  1

while count <= N:
    total_sum += M
    M += 1
    count += 1
print(total_sum)