N = int(input())
a = int(input())
if N <= 5:
    for i in range(N-1):
        a = int(not a)
        print(a)
else:
    print("Love is open door")
    
    
# int(not a)는 a의 값에 따라 0 또는 1