N, M = map(int, input().split())
M_list = list(map(int, input().split()))
answer = [0] * (N + 1)

for m in M_list:
    temp = m
    while temp <= N:
        answer[temp] = temp
        temp += m
        
print(sum(answer))