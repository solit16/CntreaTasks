n, k = [int(x) for x in input().split()]
stalls = [int(x) for x in input().split()]


def check(number):
    cows = 1
    last = stalls[0]
    for stall in stalls:
        if stall - last >= number:
            cows += 1
            last = stall
    return cows >= k


left = 0
right = stalls[-1] - stalls[0]
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
