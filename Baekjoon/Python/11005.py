N, B = map(int, input().split())
s = ""
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    s += str(arr[N % B])
    N //= B

print(s[::-1])

# 다시 풀어봐야함...(x2)
