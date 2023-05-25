nums = []
for i in range(5):
    nums.append(int(input()))
print(int(sum(nums) / len(nums)))
print(sorted(nums)[len(nums) // 2])
