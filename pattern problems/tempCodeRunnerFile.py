N = int(input())

for i in range(1,N+1):
    spaces = 2 * (N - i)
    star = 2 * i - 1
    print(' ' * spaces + '* ' * star)