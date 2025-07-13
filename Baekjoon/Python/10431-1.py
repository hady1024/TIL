p =int(input())

for k in range(1,p+1):
    height_sort = []
    height = list(map(int, input().split()))
    ans = 0
    for i in range(1,len(height)):
        if i == 1:
            height_sort.append(height[i])
            continue

        now = height[i]
        if now > max(height_sort):
            height_sort.append(now)
            continue

        for j in range(len(height_sort)):
            if height_sort[j] > now:
                height_sort.insert(j, now)
                ans += (len(height_sort) - j - 1)
                break
    print(k,ans)
    
