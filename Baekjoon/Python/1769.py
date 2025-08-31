num = input()
cnt = 0 

while len(num)>1: 
    cnt+=1 
    answer=0
    for i in num:
        answer+=int(i) 
    num =str(answer) 

print(cnt) 

if int(num)%3 ==0: 
      print("YES")
else:
       print("NO")