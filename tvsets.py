n = int(input())
R1, R2 = map(int, input().split())
target = int(input())
cost= final = 0
l2 = l1 = []
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for m in range(len(month)):
    for d in range(1, month[m] +1):
        l1.append((6 - (m + 1)) ** 2+ abs(d - 15))
    l2.append(l1)
    l1 = list()
for i in range(n + 1):
    for j in l2:
        for k in range(j):
            if k >= n:
                t = n - i
                cost += (i * R1 + t * R2)
            else:
                h = n - i
                t = k - h
                if t <= 0:
                    cost += (k*R2)
                else:
                    cost += (t * R1 + h * R2)
        final += cost
        cost = 0
    if final >= target:
        print(i)
        break
    else:
        final = 0
else:
    print(n)
