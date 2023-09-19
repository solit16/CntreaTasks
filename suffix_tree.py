suffixes = {}
s = input()

for i in range(len(s)):
	suffixes[s[i:len(s)]] = i
suffixes[''] = len(s)
res = []
for el in sorted(suffixes.keys()):
	res.append(suffixes[el])

print(*res)
