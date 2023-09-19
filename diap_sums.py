import sys
arr = []
res = []
elements_sum = 0
while True:
    line = input()
    if line == '':
        break
    arr.append([int(i) for i in line.split()])
while True:
    try:
        req = [int(i) for i in input().split()]
        for i in range(req[0], req[2] + 1):
            elements_sum += sum(arr[i][req[1]:(req[3] + 1)])
        res.append(elements_sum)
        elements_sum = 0
    except:
        break
for number in res:
    print(number)
