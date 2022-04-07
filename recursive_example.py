#factorial using function
#4!=4*3*2*1=24

def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i

    return fact     

print(factorial(4))
print(factorial(5))
print(factorial(6))


#factorial using resursive function

def factorial2(n):
    if n==1:
        return 1
    return n*factorial2(n-1)    
x= int(input('Enter a value: '))
print(factorial2(x))    