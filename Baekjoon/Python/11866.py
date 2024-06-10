from sys import stdin

N, K = map(int,stdin.readline().split())
index = 0
array = list(range(1,N+1))
result = []

while len(array) != 0: # 리스트 수가 0이 아니면 반복
    index += (K-1)
    index = index % len(array)
    result.append(array.pop(index))

print("<",end="")
for i in range(N-1):
    print(result[i],end=", ")
print(result[N-1], end = "")
print(">",end="")

# 다시 풀어보기(x2 안됐음)