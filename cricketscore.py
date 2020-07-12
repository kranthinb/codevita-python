def D_update(Dlist):
    for i in range(len(Dlist)):
        if Dlist[i] == "W":
            Dlist[i] = '-2'
    return [int(i) for i in Dlist]


def runs(D):
    sum = 0
    for i in D:
        if i != -2:
            sum += i
    return sum


def update(striker):
    if striker is True:
        striker = False
        non_striker = True
    else:
        striker = True
        non_striker = False
    return striker,non_striker


def score(D):
    global striker_runs, non_striker_runs
    overs = int(Balls% 6)
    striker = True
    non_striker = False
    for i in D:
        if striker is True:
            if i == -2:
                striker_runs = 0
            else:
                striker_runs += i
        else:
            if i == -2:
                non_striker_runs = 0
            else:
                non_striker_runs += i
        overs += 1
        if i % 2 != 0:
            striker, non_striker = update(striker)
        if overs == 6:
            striker, non_striker = update(striker)
            overs = 0
    if striker is True:
        return striker_runs,non_striker_runs
    else:
        return non_striker_runs,striker_runs


RR1 = float(input())
striker_runs, non_striker_runs = map(int,input().split())
D = input().split()
RR2 = float(input())
D = D_update(D)
sum_D = runs(D)
Balls = (RR2* len(D) - 6*sum_D) // (RR1 - RR2)
Runs = int(RR1 * Balls//6)
strikerRuns, non_strikerRuns = score(D)
total_runs = Runs + sum_D
print(total_runs,strikerRuns,non_strikerRuns)
