import sys
a, b, c = [int(x) for x in sys.stdin.read().strip().split()]
if b < 0:
    a, b, c = -a, -b, -c

def nod(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return abs(num1)

def step(num1, num2):
    res = []
    div = num1[0] // num2[0]
    for i in range(len(num1)):
        if i == 0:
            res.append(num1[0] % num2[0])
            continue
        res.append(num1[i] - div * num2[i])
    return num2, res

def extended_euclid(nums):
    first, second = nums[:len(nums) // 2], nums[len(nums) // 2:]
    while second[0] != 0:
        first, second = step(first, second)
    return first + second

if c % nod(a, b) != 0:
    print('NO SOLUTIONS')
else:
    nod_of_all = nod(nod(a, b), c)
    if nod_of_all != 1:
        a, b, c = a // nod_of_all, b // nod_of_all, c // nod_of_all
    num = extended_euclid([a, c, b, 0])[1]
    if b != 0:
        print(f'x = {num % b} + {b}k')
        print(f'y = {(c - a * (num % b)) // b} - {a}k')
    else:
        print(f'x = {c // a} + {b}k')
        print(f'y = 0 - 1k')
