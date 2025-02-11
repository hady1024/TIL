n,t = map(int,input().split())
fcfs = list(map(int,input().split()))
r = 0
for i in fcfs:
    t -= i
    if t>=0:
        r+=1
    else:
        break
print(r)