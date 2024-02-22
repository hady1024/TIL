A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

if P > C:
    result = B + (P-C)*D
else:
    result = B

print(min(A*P, result))
