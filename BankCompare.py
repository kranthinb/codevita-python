def emi(principal,year,roi):
    amount = (principal * roi)/(1-1/((1+ roi)**(year*12)))
    return amount


p = int(input())
t = int(input())
bank = []
for i in range(2):   #for bank A and bank B
    sum = 0
    n = int(input())
    for i in range(n):
        period, roi = list(map(float,input().split()))
        sum += emi(p,int(period),roi)
    bank.append(sum)
if bank[0] < bank[1]:
    print("Bank A")
else:
    print("Bank B")

