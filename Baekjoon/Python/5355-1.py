def calc(num, item):
    if item == '@' : return num * 3
    elif item == '%' : return num + 5
    elif item == '#' : return num - 7

n = int(input())

for _ in range(0, n):
    A = list(input().split(" "))
    num = float(A.pop(0))

    for i in A:
        num = calc(num, i)
    print("%.2f" % num)

# 함수 사용시 풀이 (참고한것 다시해보기)