n = int(input())

for _ in range(n) :
  data = list(input().split())
  for i in range(2, len(data)) :
    print(data[i], end=' ')
  
  print(data[0], data[1])