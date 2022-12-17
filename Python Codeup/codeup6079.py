sum = 0
i = 0
n = int(input())
while True:
    i += 1
    sum += i
    if sum >= n:
        print(i)
        break
