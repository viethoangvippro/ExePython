import math
print("x : ")
x = float(input())
print ("k : ")
k = int(input())
first = 0.5
temp = 2
second = -1*first - (math.pow(x,temp)/temp)
		
while math.fabs(first - second) > 10 ** (-k)  :
    temp = temp + 1
    first = second
    second = first - (math.pow(x,temp)/temp)
    
print(f'{second:.3f}')