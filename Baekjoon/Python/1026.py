N = int(input())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

A_lst = sorted(A_lst, reverse=True)
B_lst.sort()

result = 0
for i in range(N):
    result += A_lst[i] * B_lst[i]
print(result)
