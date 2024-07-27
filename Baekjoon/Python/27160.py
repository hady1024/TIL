import sys
from collections import deque

N = int(input())

my_dict = {
    "STRAWBERRY" : 0,
    "BANANA" : 0,
    "LIME" : 0,
    "PLUM" : 0
}

for i in range(N):
    V, A = input().split()
    my_dict[V] = my_dict[V] + int(A)

X = my_dict["BANANA"]
Y = my_dict["LIME"]
Z = my_dict["PLUM"]
K = my_dict["STRAWBERRY"]

if X == 5 or Y == 5 or Z == 5 or K ==5 :
    print("YES")
else:
    print("NO")

# 딕셔너리 활용