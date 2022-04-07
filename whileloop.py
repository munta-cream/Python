"""
while loop
==================
initialize variable
while condition:
    statements
    increment

"""

# x=0 #initialize variable 
# while x<=5 :   #x<5 - Condition 
#     print(x, end='\t')   #statement 
#     x = x+1 #increment 

# x=50 #initialize variable 
# while x>=40 :   #x<5 - Condition 
#     print(x, end='\t')   #statement 
#     x = x-1 #increment 

x=1 
while x<=30 :
    if x%2==0:
        print(x,end='\t')
    x = x+1 

#check Prime Number
num=17
x=2
isPrime=True
while x<num :
    if num % x==0:   
        isPrime=False
        break 
    x = x+1

if isPrime :
    print('Prime Number')
else :
    print('Not a Prime Number')
    

# Sum of Series
sum=0
x=1 
while x<=10 :
    sum =sum +x
    # x - x+1
    x +=1

print(sum)

# Sum of Series
#1+2+3+4+5+6+7+8+9+10
sum=0
x=1 
while x<=10 :
    sum =sum +x**2
    # x - x+1
    x +=1

print(sum)