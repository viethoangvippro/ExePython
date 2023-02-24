import math
print("x : ")
x = float(input())
print ("k : ")
k = int(input())


first = 1 
mu = 1 
second = first + (x/1)


while math.fabs(first - second ) >  10 ** (-k)   :
    mu = mu+1
    first = second
    second = first + ( x**mu / mu)

print(f'{first:.3f}')