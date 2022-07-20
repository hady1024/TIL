import sys

sys.stdin = open("input.txt", "r")

alphabets = input()

for i in range(len(alphabets)) :
    print(ord(alphabets[i])-64, end=' ')