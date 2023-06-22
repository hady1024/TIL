n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x * int(cnt), end="")
    print()

# 다시 풀어보기
