while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    lst.sort()
    if lst[2] ** 2 == lst[0] ** 2 + lst[1] ** 2:  
        print("right")
    else:
        print("wrong")

# 다시 풀어보기
