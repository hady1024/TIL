# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

number = 123

result = 0
while number:
    result += number%10
    number //= 10

print(result)