import math
first = 1
x = 0.5		
mu = 1
dau = -1
eps = 0.000001

temp = (0.5)*math.pow(x,mu)
second = first + (0.5)*math.pow(x,mu)
while(math.fabs(first - second) > eps ) :
    tu = 1
    mau = 4
    mu-=-1
    n=mu
    temp= (0.5)*math.pow(x,mu)
    first = second
    while(n>1) :
        temp = temp*(tu/mau)
        tu= tu+2
        mau=mau+2
        n= n -1
        second =  first + dau*temp
        dau = - dau
print(second)