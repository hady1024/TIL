import sys
input = sys.stdin.readline

yeondu = list(input().rstrip())
n = int(input())
scoreBoard = {}

for _ in range(n):
    team = input().rstrip()
    nowScore = 1
    scores = []

    for name in ['L', 'O', 'V', 'E']:
        scores.append(team.count(name) + yeondu.count(name))

    for i in range(len(scores)):
        for j in range(i+1, len(scores)):
            nowScore *= (scores[i] + scores[j])

    scoreBoard[team] = nowScore % 100

scoreBoard = list(scoreBoard.items())
scoreBoard.sort(key=lambda x: x[0])
scoreBoard.sort(key=lambda x: x[1], reverse=True)

print(scoreBoard[0][0])

# 다시 풀어보기