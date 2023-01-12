n = int(input())
game = [[0 for _ in range(19)] for _ in range(19)]

for i in range(n):
    a, b = map(int, input().split())
    game[a - 1][b - 1] = 1

for i in range(19):
    for j in range(19):
        print(game[i][j], end=" ")
    print()
