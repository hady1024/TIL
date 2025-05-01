a, b = list(map(int, input().split()))

for x in range(-1000, 1001):
    if x * x + 2 * a * x + b == 0:
        print(x, end=" ")