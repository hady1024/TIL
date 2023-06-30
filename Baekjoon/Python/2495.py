for _ in range(3):
    s = str(input())
    i_max = 1
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            i_max = max(cnt, i_max)
            cnt = 1
    i_max = max(cnt, i_max)
    print(i_max)
