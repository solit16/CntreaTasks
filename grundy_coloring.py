from functools import cache

@cache
def grundy_single(n):
	reachable = set()

	for left in range(n - 1):
		right = n - 2 - left
		reachable.add(grundy_single(left) ^ grundy_single(right))
	for x in range(len(reachable) + 1):
		if x not in reachable:
			return x
if grundy_single(int(input())) == 0:
	print(2)
else:
	print(1)
