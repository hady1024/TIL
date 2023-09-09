n = int(input())
test = list(map(int, input().split()))
a, b = map(int, input().split())

cnt = n
for i in test:
    i -= a
    if i > 0:
        if i % b:
            cnt += (i // b) + i
        else:
            cnt += i // b


print(cnt)
