from functools import cache
@cache
def domino(n):
	if n % 2 == 1:
		return 0
	if n == 0:
		return 1
	if n == 2:
		return 3
	return 4*domino(n-2) - domino(n-4)

print(domino(int(input())))
