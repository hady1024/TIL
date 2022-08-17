N = int(input())

if N == 1:
    print('*')

else:
    for i in range(N):
        if i % 2 == 0:
            a = print('* ' * N)
        else:
            b = print(' *' * N)
