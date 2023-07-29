# 다른 사람의 풀이
T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i - 1] == "1":
            print(i, end=" ")

# 다시 풀어보기
