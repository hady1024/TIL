n = int(input())

cnt = 0
i = 0
while True:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

    if n < 0:  # 2백원씩 뺏더니 음수가 되버린경우 --> 거슬러 줄 수 없을을 의미
        break
if n < 0:
    print(-1)
else:
    print(cnt)



