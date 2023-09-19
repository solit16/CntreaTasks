import sys

def neighbors(graph, vertex):
    return list(graph[vertex]) if vertex in graph else []


def solve(graph):
    stack = [(0, 0)]
    visited = set()
    binds = {}
    while stack:
        cur = stack.pop()
        if cur[0] in visited: 
            continue
        if cur[0] != 0:
            binds[cur[0]] = cur[1]
        visited.add(cur[0])
        stack = [(x, cur[0]) for x in neighbors(graph, cur[0]) if x not in visited][::-1] + stack
    if 1 not in binds:
        return None
    res = [1]
    start = 1
    while start != 0:
        res.append(binds[start])
        start = binds[start]
    return res[::-1]

exec(sys.stdin.read())
