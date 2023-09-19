import sys

def extended_euclid(first, second):
    while second[0] != 0:
        new_b = [first[i] - (first[0] // second[0]) * second[i] for i in range(len(first))]
        first, second = second, new_b
    return first[:], second[:]

a, A, b, B, n = [int(x) for x in sys.stdin.read().split()]

l1, l2 = extended_euclid([a, A], [b, B])

if l2[1] % n == 0:
    print(l1[1] % n)
