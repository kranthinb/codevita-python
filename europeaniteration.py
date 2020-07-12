def romanConverter(num):
    div = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    i = 0
    rnum = ""
    while num > 0:
        for _ in range(num // div[i]):
            rnum += roman[i]
            num -= div[i]
        i += 1
    return rnum


n = int(input())
pvs = {'C': 12, "D": 13, "I": 18, "L": 21, "M": 22, "V": 31, "X": 33}
while 1 <= n <= 3999:
    r = romanConverter(n)
    base = 0
    for i in r:
        if pvs[i] > base:
            base = pvs[i]
    p = 0
    n = 0
    for i in r[::-1]:
        n += pvs[i] * ((base+1) ** p)
        p += 1

print(n)
