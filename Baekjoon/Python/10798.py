words =[input() for _ in range(5)]
result=''

for i in range(15):
  for j in range(5):
    if i <= len(words[j])-1:
      result += words[j][i]
print(result)