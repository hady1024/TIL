# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# sum() 함수 사용 금지

# while

n=int(input())
i = 0
sum = 0
while i< n:
    i += 1
    sum += i
print(sum)


# for

n=int(input())
i = 0
sum = 0
for i in range(n):
    i += 1
    sum += i
print(sum)