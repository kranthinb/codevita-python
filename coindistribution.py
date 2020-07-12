def two_one(remainder):
    if remainder % 2 == 0:
        remainder -= 2
        two = remainder // 2
        one = 2
        return two, one
    else:
        two = remainder // 2
        one = 1
        return two, one


n = int(input('Enter a value: '))
if n == 0:
    five_value, two_value, one_value = 0, 0, 0
elif n < 9:
    five_value = 0
    two_value, one_value = two_one(n)
elif n % 10 == 4 or n % 10 == 9:
    five_value = n // 5
    two_value, one_value = two_one(n % 5)
else:
    n_dec = n - 5
    five_value = n_dec // 5
    two_value, one_value = two_one(n_dec % 5 + 5)

total = five_value + two_value + one_value
print(total, five_value, two_value, one_value)

# Other method to find minimum coin distribution
five = int((n - 4) / 5)
if ((n - 5 * five) % 2) == 0:
    one = 2
else:
    one = 1

two = (n - 5 * five - one) // 2

print(five+two+one, five, two, one)
