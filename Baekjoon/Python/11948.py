n = []
for _ in range(6):
    n.append(int(input()))
n1 = sorted(n[:4])
n2 = n[4:]
print(sum(n1[1:]) + max(n2))
