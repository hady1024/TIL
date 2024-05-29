import sys
temp=0
n=int(input())
nums=list(map(int,sys.stdin.readline().split())) 

for i in nums:
    for value in nums:
        temp+=abs(i-value)
print(temp)