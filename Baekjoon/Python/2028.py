N = int(input())

for _ in range(N):
    num = int(input())
    k = len(str(num)) 
    if str(num**2)[-k:] == str(num): 
        print("YES")
    else:
        print("NO")

# 참고한것 다시 풀어보기