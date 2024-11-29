N = int(input())

for i in range(N, 0,-1):
    spaces = N - i
    if i == N:
        print(spaces * " " + "+ " * i)
    else:
        print(spaces * " " + "* " * i)