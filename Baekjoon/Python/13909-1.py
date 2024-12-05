import sys
N = int(sys.stdin.readline())
result = 0
x = 1
while x*x <= N:
    x += 1
    result +=1
print(result)

# 다른 사람 풀이 (다시해보기)