n = int(input())
t = int(input())
m = 0
max_steps = 0
p = []
max_win = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(2, t + 1, 2):
    for j in range(len(p)):
        n = 0
        sum = 0
        for k in range(i):
            sum += p[j][k] * p[j][-1]
        if sum > max_steps:
            max_steps = sum
            m = j + 1
    max_win.append(m)
print(max(set(max_win), key=max_win.count))
print()
