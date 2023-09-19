import sys

def extended_euclid(first, second):
    while second[0] != 0:
        new_b = [first[i] - (first[0] // second[0]) * second[i] for i in range(len(first))]
        first, second = second, new_b
    return first[:], second[:]

a, A, b, B = [int(x) for x in sys.stdin.read().split()]

l1, l2 = extended_euclid([b, A*b], [a, B*a])

if l2[1] % (a*b) == 0:
    print(l1[1] % (a*b))
