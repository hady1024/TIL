# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = 'banana'

result = {}
for char in word:
    if not char in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1
print(result)

# 위의 풀이법은 강의시간 풀이법 보고 한 것입니다. ㅠ