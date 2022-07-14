# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

word = input()
result = ''
for i in word:
    number = ord(i)
    number = number -32
    result += chr(number)
print(result) 


# 강의 시간에 알려준 다른 방법

for char in word:
    print(chr(ord(char)-32), end='')






    
