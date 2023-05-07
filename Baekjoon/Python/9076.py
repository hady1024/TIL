n = int(input())  # 반복 횟수를 입력


for i in range(n):  # n만큼 반복

    score = list(map(int, input().split()))  # 점수를 입력받는 즉시 리스트에 저장

    score.sort()  # 입력받은 점수를 오름차순 정렬

    if score[3] - score[1] >= 4:  # 5개의 점수중[0,1,2,3,4] 1번째와 3번째의 차이가 4점 이상일 때

        print("KIN")  # KIN을 출력

    else:  # 아닐경우

        print(sum(score) - min(score) - max(score))
