L, R, A = map(int, input().split())
total = L + R + A

if L > R :
    L, R = R, L

if L == R :
    if A % 2 != 0 :
        total -= 1
else :
    if A < (R - L) :
        total -= abs((L+A) - R)
    elif A > (R - L) :
        A -= (R - L)
        if A % 2 != 0 :
            total -= 1    

print(total)
