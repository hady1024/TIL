R, C, ZR, ZC = map(int, input().split())
paper = [input() for _ in range(R)]
scanner = []

for i in range(R):
    row = []
    for j in range(C):
        row.append(paper[i][j] * ZC)
    for _ in range(ZR):
        scanner.append(row)

for s in scanner:
    print("".join(s))

