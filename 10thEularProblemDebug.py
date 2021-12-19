# solve it for input 2000000 -- 2million
n = int(input('Enter the range for prime below 1 to '))
prime = []
for i in range(1, n):
    count = 0
    for p in range(2, i):
        if i % p == 0:
            break
        else:
            count += 1

    if (count + 2) == i:
        # print('number', i, ' is prime')
        prime.append(i)

# print()

# print('all prime will be ')
# print(prime)
print('sum of all prime will be =', sum(prime))
