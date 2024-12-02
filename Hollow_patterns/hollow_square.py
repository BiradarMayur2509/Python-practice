N = int(input())

for i in range(1,N+1):
    if (i == 1 or i == N):
        row = "* " * N
    else:
        spaces = " " * (2* N - 4)
        row = "* " + spaces + "* "
    print(row)