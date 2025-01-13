line = input()
rst = []
i = 0
while i < len(line):
    if line[i] in ['a','e','i','o','u']:
        rst.append(line[i])
        i += 3
    else:
        rst.append(line[i])
        i += 1

print(''.join(rst))