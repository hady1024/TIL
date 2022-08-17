N = int(input())
hansu = 0

for i in range(1, N+1) :
    if i <= 100 : 
        hansu += 1 
    
    else :     
        nums = list(map(int, str(i))) 
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            hansu+=1