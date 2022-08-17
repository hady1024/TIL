while True:
    A, B = map(int, input().split())
    if (A == 0 and B == 0):
        break
    print(A + B)


    # while 문으로 돌리고 A B를 정수로 받고 if문으로 A B가 0이면 break로 while문 빠져나오고 A+B 합을 출력