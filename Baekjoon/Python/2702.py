import math


def lcm(a, b):
    return int((a * b) / gcd(a, b))


def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))

# 다시 풀어보기

# 2
def lcm(a, b):
    return (a * b) // math.gcd(a, b)


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(lcm(n, m), end=" ")
    print(math.gcd(n, m))

# 다시 풀어봐야함..
