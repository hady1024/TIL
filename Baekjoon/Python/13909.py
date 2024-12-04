import sys

N = int(sys.stdin.readline())

num = 0
while ((num + 1) ** 2 <= N):
    num += 1

print(num)