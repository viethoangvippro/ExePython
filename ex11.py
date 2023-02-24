import math
print("x : ")
x = float(input())
print ("k : ")
k = int(input())

mu = 2
first = x
second = first + (x ** mu / mu) * (-1) ** (mu + 1)

while math.fabs(first - second) > 10 ** (-k) :
    mu = mu + 1
    first = second
    second = first + (x ** mu / mu) * (-1) **(mu +1)

print(f'{first:.3f}')