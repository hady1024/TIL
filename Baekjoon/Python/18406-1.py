n = list(map(int, input()))
half = int(len(n) / 2)

if sum(n[:half]) == sum(n[half:]):
    print("LUCKY")
else:
    print("READY")