y=list(input())
a=['E','S','T','J']
b=['I','N','F','P']
for i in range(len(y)):
    if y[i]==a[i]:
        print(b[i],end='')
    else:
        print(a[i],end='')