def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

x = 0.5
eps = 0.000001
mu = 1
dau = -1
first = 1
second = first - x**(mu + 1) / fac(mu + 2)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**(mu + 1) / fac(mu + 2))
    dau = -dau
print("KQ: ", second)