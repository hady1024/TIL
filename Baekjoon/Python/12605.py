n = int(input())
for i in range(n):
	n_list = list(input().split())
	n_list = n_list[::-1]
	s = ' '.join(n_list)
	print("Case #%d: %s" %(i+1, s))