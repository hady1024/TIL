A=int(input())
user = []
for _ in range(A):
    age, name = input().split()
    user.append([int(age),name])

for i in sorted(user):
    print(i[0],i[1])