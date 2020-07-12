from itertools import permutations


n1 = input("Enter a value: ")
n2 = input("Enter another value: ")
list1 = list(n1)
list1.sort()
list2 = list(n2)
list3 = list()
if len(list1) == len(list2):
    value_2 = int(''.join(list2))
    list_per = list(permutations(list1))
    for i in range(len(list_per)):
        value_per = int(''.join(list_per[i]))
        if value_per > value_2:
            print(value_per)
            break
        else:
            continue
    else:
        print('-1')
else:
    print('-1')
