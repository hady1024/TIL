n = int(input())  

ab = input()  
m=0
score_A = 0  
score_B = 0  
for i in ab:
    if i=="A":
        n-=1  
        m+=1  

if m>n:
    print("A")
elif m<n:
    print("B")
else:
    print("Tie")