# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100, 40]
max_number = numbers[0]
second_number = numbers[0]

for n in numbers:
    if max_number < n:
        second_number = max_number
        max_number = n
    elif second_number < n and n < max_number:
        second_number = n
        print(second_number)

        # 줌 수업 해설 듣고 적었습니다. 다시 해봐야겠습니다