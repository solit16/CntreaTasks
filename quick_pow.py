a, b = [int(x) for x in input().split()]
res = 1
step = a
while b != 0:
    if b % 2 == 1:
        res *= step
    step *= step
    b //= 2
print(res)
