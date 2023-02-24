import math
print("x : ")
x = float(input())
print ("k : ")
k = int(input())
first = 1
temp = 1
dau = -1
second = first +dau*(((temp+1)*(temp+2))/2) * math.pow(x,temp)
while math.fabs(first - second) > 10 ** (-k)  :
    temp = temp +1
    dau = - dau
    first = second
    second = first +dau*(((temp+1)*(temp+2))/2) * math.pow(x,temp)

print(f'{second:.3f}')