N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_bundle = 0
for sz in size:
  if sz == 0:
    continue
  elif sz <= T:
    shirt_bundle += 1
  elif sz % T == 0:
    shirt_bundle += (sz // T)
  else:
    shirt_bundle += (sz // T) + 1

print(shirt_bundle)
print(N//P, N%P)

# 다시 해보기 