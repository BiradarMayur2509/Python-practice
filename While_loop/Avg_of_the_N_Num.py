# write a program that reads a number N and prints the average of N numbers from 1.
# The program should ask for user input and then print the average of the numbers from 1 to N.
# input : N = 4
# output : 2.5
# use while loop to solve this problem.

N = int(input())
initial_N = N
total_sum = 0

while N > 0:
    total_sum = total_sum + N
    N = N - 1
print(total_sum / initial_N)

