# Given an integer N , write a program which reads N inputs and print the sum of the given inputs in integers.
# use while loop to solve this problem.

N = int(input())

total_sum = 0
count = 1

while count <= N:
    number = int(input())
    total_sum = total_sum + number
    count = count + 1
print(total_sum)