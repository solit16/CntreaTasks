Memo = {}

def solve(n):
    if n == 1:
        Memo[n] = 1
        return
    if n == 2:
        Memo[n] = 2
        return
    Memo[n] = Memo[n-2] + Memo[n-1]
    return

N = int(input())
for k in range(1, N + 1):
    solve(k)
print(Memo[N])
