import numbers
import sys

sys.stdin = open("input.txt", "r")

T=int(input())


for i in range(1,T+1):
    numbers= []
    numbers =map(int, input().split())
    average = round(sum(numbers) /10)

    print(f'#{i} {average}')




