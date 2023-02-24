def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

first = 1
x = 0.5
mu = 1
dau = -1
eps = 0.00001
n = 0
temp = 1
second = first - (0.5)*x**mu
while abs(first - second) > eps:
    tu = 3
    mau = 4
    mu -= -1
    n = mu
    temp = (0.5) * x**mu
    first = second
    while(n>1):
        temp = temp * (tu/mau)
        tu = tu + 2
        mau = mau + 2
        n-=1
    dau = -dau
    second = first + dau*temp
print("KQ: ", second)  