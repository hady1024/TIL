for _ in range(int(input())):
    list = input().split()
    a, b, c = int(list[0]), int(list[2]), int(list[4])
    op = list[1]
    if op == '+':
        t = a+b
    elif op == '-':
        t = a-b
    elif op == '*':
        t = a*b
    elif op == '/':
        t = a//b
    print("correct" if t == c else "wrong answer")