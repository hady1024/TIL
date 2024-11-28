e,f,c=map(int,input().split())
i=0;e+=f
while e>=c:
 p,q=e//c,e%c
 e=p+q
 i+=p
print(i)