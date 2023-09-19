import sys
nums = [int(x) for x in sys.stdin.read().strip().split()]
first, second = nums[:len(nums) // 2], nums[len(nums) // 2:]
def step(a, b):
    res = []
    div = a[0] // b[0]
    for i in range(len(a)):
        if i == 0:
            res.append(a[0] % b[0])
            continue
        res.append(a[i] - div * b[i])
    return b, res

while second[0] != 0:
    first, second = step(first, second)

print(*first)
print(*second)
