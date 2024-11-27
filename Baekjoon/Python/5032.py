e, f, c = map(int, input().split())
n = (e+f)//c + (e+f)%c
res = (e+f)//c
while n//c:
    res += n//c
    n = n//c + n%c
print(res)


# 2
e,f,c=map(int,input().split())
i=0;e+=f
while e>=c:
 p,q=e//c,e%c
 e=p+q
 i+=p
print(i)

