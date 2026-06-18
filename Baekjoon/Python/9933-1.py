tmp=[]
for _ in range(int(input())):
    tmp.append(input())
for i in tmp:
    if i[::-1] in tmp: print(len(i),i[len(i)//2]) ; break
    
