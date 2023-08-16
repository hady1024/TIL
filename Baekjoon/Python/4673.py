def self_number():
    range_numbers = set(range(1, 10001))
    non_self_numbers = set()

    for num in range(1, 10001):
        for each_num in str(num):
            num += int(each_num)

        non_self_numbers.add(num)

    return sorted(range_numbers - non_self_numbers)


if __name__ == "__main__":
    self_numbers = self_number()

    for self_num in self_numbers:
        print(self_num)

# 다시 풀어보기
