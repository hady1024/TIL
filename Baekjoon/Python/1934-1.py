T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    result = A * B

    while B > 0:
        A, B = B, A % B

    print(result // A)

    # 다시 해보기
