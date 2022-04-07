
from re import X


def fact(n):
    if n==0:
        return 1 
    else:
        return n*fact(n-1)
print(fact(5))

print(fact(4))


fact=1
num=5 
for z in range(1,num+1):
    fact=fact*X

print(fact)