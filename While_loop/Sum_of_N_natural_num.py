# Write a program that reads a number N and prints sum of N natural numbers.
# input n = 5
# output 15
# use while loop to solve this problem.

n = int(input())

total_sum = 0

while n > 0:
    total_sum = total_sum + n
    n = n - 1
print(total_sum)