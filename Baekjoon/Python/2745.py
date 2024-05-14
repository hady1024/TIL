num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
answer = 0
for i, num in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.index(num)
print(answer)

# 다른 풀이 더 쉽게 하는방법 있다고 함 다시 풀어보기