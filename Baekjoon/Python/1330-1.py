x, y = map(int, input().split())

result = x - y

if result > 0:
    print(">")

elif result < 0:
    print("<")

else:
    print("==")
