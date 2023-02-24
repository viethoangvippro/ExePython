def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

x = 0.5
eps = 0.0000001
mu = 2
first = 1
second = first + x**mu / fac(mu)
while abs(first - second) > eps:
    mu += 2
    first = second
    second = first + x**mu / fac(mu)
print("KQ: ", second)