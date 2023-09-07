A, B = map(int, input().split())
dec = int(bin(A ^ B)[2:], 2)
print(dec)
