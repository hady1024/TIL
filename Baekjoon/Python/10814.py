import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    arr.append([int(a), b])

arr.sort(key=lambda x: x[0])

for i in arr:
    print(*i, sep=" ")
