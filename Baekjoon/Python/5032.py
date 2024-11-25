e, f, c = map(int, input().split())
n = (e+f)//c + (e+f)%c
res = (e+f)//c
while n//c:
    res += n//c
    n = n//c + n%c
print(res)


# 
e,f,c=map(int,input().split())
i=0;e+=f
while e>=c:
 p,q=e//c,e%c
 e=p+q
 i+=p
print(i)

# 참고한것 다시풀어보기