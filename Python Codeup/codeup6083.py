r, g, b = map(int, input().split())

count = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print("%d %d %d" % (i, j, k))

            count = count + 1

print(count)
