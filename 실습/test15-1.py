# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

word =input()

for i in range(len(word)):
    if word[i]== 'a':
        print(i,end=' ')

    