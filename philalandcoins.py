#Number of test cases to be executed
t = int(input(""))
for i in range(t):
    n = int(input(""))
    coins_count = 0
    while n >= 1:
 # We can generate any number by using the logic of combination of powers of 2
        n = n // 2
        coins_count += 1
    print(coins_count)

 
