N = int(input())

result = [N]
for i in range(1, N+1) :
  tmp = [N, i]
  while tmp[-1] >= 0 :
    tmp.append(tmp[-2] - tmp[-1])
  tmp.pop()
  if len(tmp) > len(result) :
    result = tmp

print(len(result))
print(*result)

# 참고한것 다시 풀어보기 (x2)