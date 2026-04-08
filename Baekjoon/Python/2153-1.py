s = input()

sum_value = 0
for i in range(len(s)) :
  if ord(s[i]) >= 97 :
    sum_value += int(ord(s[i]) - 96)
  else :
    sum_value += int(ord(s[i]) - 38)

flag = 0
for i in range(2, int(sum_value**0.5) + 1) :
  if sum_value % i == 0 :
    flag = 1

if flag == 0 :
  print("It is a prime word.")
else :
  print("It is not a prime word.")

# 다시 해보기