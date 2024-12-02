ans = 0
n, d = map(int, input().split())
for i in range(1, n+1):
    ans += str(i).count(str(d))
print(ans)