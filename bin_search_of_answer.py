def checker(some_list, number, checking):
    counter = 0
    some_list_copy = some_list[:]
    for num in some_list_copy:
        while num > 0:
            num -= checking
            if num >= 0:
                counter += 1
    if counter >= number:
        return True
    else:
        return False


n, k = [int(x) for x in input().split()]
lens = []
for i in range(n):
    lens.append(int(input()))

left = 0
right = max(lens)
mid = (left + right) // 2
while left < right:
    if n == 1 and k == 1:
        print(lens[0])
        break
    if checker(lens, k, mid):
        left = mid
        mid = (left + right) // 2
    else:
        right = mid
        mid = (left + right) // 2
    if left == mid:
        print(mid)
        break
