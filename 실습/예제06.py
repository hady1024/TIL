# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# 'tuple' object has no attribute 'append' 튜플에선 append를 쓸 수 없다 리스트는 []로

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)