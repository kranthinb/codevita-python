def is_prime(num):
  # return TRUE if num is prime
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True


n = int(input())
sum = count = 0
for i in range(2,n+1):
    if is_prime(i):
        sum += i
        if is_prime(sum) and sum > 2:
            count +=1

print(count)
