a, b, v = map(int, input().split())
k = 0  # 올라가는 데 걸리는 날짜 수
d = 0  # 올라간 높이
while 1:
    k += 1
    if a * k - b * (k - 1) >= v:
        break
print(k)
