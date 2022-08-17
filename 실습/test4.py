# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# while

n=int(input())
i = 0
result = 1
while i< n:
    i += 1
    result *= i
print(result)



# for

n=int(input())
i = 0
result = 1
for i in range(n):
    i += 1
    result *= i
print(result)