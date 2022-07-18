# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max > max2:
    # print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max < max2:
    # print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
    # print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 'int' object is not callable 타입에러가 발생하여 max함수 중복으로 인해 
# max = max(number_list), max2 = max(number_list2) 여기서
# max 함수 중복으로 max를 삭제 max = (number_list), max2 = (number_list2)

number_list = [1, 23, 9, 6, 91, 59, 29]
max = (number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = (number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")