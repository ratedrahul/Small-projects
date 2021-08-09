import random
x = int(input("Enter value of first number "))
y = int(input("Enter value of second number "))

if y < x:
    y, x = x, y
number = []
numb2 = []

for i in range(x - 1):
    p = x % (i + 1)
    if p == 0:
        numb2.append(i + 1)
print('Divisor of first number {} will be :\n '.format(x), numb2)

for i in range(y - 1):
    q = y % (i + 1)
    if q == 0:
        number.append(i + 1)
print('Divisor of second number {} will be: \n '.format(y), number)


l = (numb2)
k = (number)
gcd = []
for i in range(len(l)):
    for j in range(len(k)):
        if l[i] == k[j]:
            gcd.append(l[i])
print('Both have these common divisors ', gcd)
GCD = max(gcd)
print("GCD of both numbers will be : ", GCD)


LCM = (x * y) / (GCD)

print("LCM of both numbers will be : ", LCM)

product = LCM * GCD

print("Product of both numbers will be : ", product)
print('yo')


# gcd=[]
# for i in range(len(l)):
# 	if l[i]==k[i]:
# 		gcd.append(k[i])
# print(max(gcd))

# for i in range(len(k)):
# 	if l[i-1]==k:
# 		u=l[i]
# 	print(u)

# for i in range(5):
# 	gcd=[]
# 	if l[i]==k[i]:
# 		gcd.append(l[i])
# 		print('GCD of both number will be',k[i],l[i])
# 		print(gcd)
# print(l,k)
