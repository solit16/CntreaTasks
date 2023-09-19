import sys

d = {}
arr = [int(x) for x in sys.stdin.read().split()]
arr2 = []
for i in range(0, len(arr) - 1, 2):
    arr2.append([arr[i], arr[i + 1]])
for line in arr2:
    if len(line) == 0:
        break

    if line[0] not in d:
        d[line[0]] = []
        d[line[0]].append(line[1])
    else:
        if line[1] not in d[line[0]]:
            d[line[0]].append(line[1])

    if line[1] not in d:
        d[line[1]] = []
        d[line[1]].append(line[0])
    else:
        if line[0] not in d[line[1]]:
            d[line[1]].append(line[0])
for i in d:
    d[i].sort()

visited = {}
stack = [1]
while stack:
    print(*stack)
    n = stack.pop()
    if n in visited:
        continue
    visited[n] = True
    stack.extend(sorted(d[n]))
