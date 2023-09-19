from functools import cache


def neighbors(sost):
	a, b = sost
	if (a == 0 or b == 0):
		return []
	res = [(a-1, b), (a-2, b), (a-3, b), (a, b-1), (a, b-2), (a, b-3)]
	if a % 2 == 0:
		res.append((a // 2, b))
	if b % 2 == 0:
		res.append((a, b // 2))
	return [(x, y) for x, y in res if (x >= 0 and y >= 0)]

@cache
def game(sost):
	pos_all = [game(x) for x in neighbors(sost)]
	pos_win = [x[1] for x in pos_all if x[0] == 1]
	pos_lose =[x[1] for x in pos_all if x[0] == 0]
	if len(pos_lose) == 0:
		if len(pos_win) == 0:
			return 0, 0
		return 0, max(pos_win)
	return 1, min(pos_lose) + 1



count = 0
n = int(input())
for i in range(1, n):
	a, b = i, n - i
	# print(a, b)
	if game((a, b))[0] == 1:
		count += 1
print(count)
