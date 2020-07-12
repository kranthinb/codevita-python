def tax_estimation(n):
    global slabs_tax
    x = 0
    for i in range(1, len(n)):
        x += int((n[i] - n[i - 1]) * tax[i - 1] // 100)
        slabs_tax.append(x)


def totalSalary():
    global total_paid
    for i in range(len(tax_paid)):
        sum = 0
        for j in range(len(slabs_tax)):
            if tax_paid[i] <= slabs_tax[j]:
                sum += slabs[j - 1]
                rem_tax = tax_paid[i] - slabs_tax[j - 1]
                rem_amt = rem_tax * 100 // tax[j - 1]
                total_paid += (rem_amt + rebate + sum)
                break
        else:
            sum += slabs[-1]
            rem_tax = tax_paid[i] - slabs_tax[-1]
            rem_amt = rem_tax * 100 // tax[-1]
            total_paid += (rem_amt + rebate + sum)


slabs = list(map(int, input().split()))
tax = list(map(int, input().split()))
rebate = int(input())
tax_paid = list(map(int, input().split()))
slabs_tax = [0]
tax_estimation(slabs)
total_paid = 0
totalSalary()
print(total_paid)
