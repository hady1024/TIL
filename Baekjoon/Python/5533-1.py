N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    s = 0
    for j in range(3):
        t = li[i][j]
        ok = 1
        for k in range(N):
            if k == i:
                continue
            if li[k][j] == t:
                ok = 0; break
        if ok == 1:
            s += t
    print(s)