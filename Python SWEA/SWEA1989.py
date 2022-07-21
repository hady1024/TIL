import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1) :
    word = input()
    for i in range(len(word)//2) :
        if word[i] == word[-1-i] :
            answer = 1
        else :
            answer = 0
    print("#{} {}".format(t, answer))
