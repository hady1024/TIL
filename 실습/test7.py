# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

numbers = [1, 20, 100]
min = numbers[1]

for i in numbers:
    if min >= i:
        min = i
print(min)