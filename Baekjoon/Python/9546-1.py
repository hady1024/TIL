import sys

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    print(2 ** k - 1)