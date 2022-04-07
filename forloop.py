"""
For loop
=================

for var in collection
    statements
        '''
"""

for x in range(6): 
    print(x,end='\t')

print("\n\n#####################\n\n")
for x in range (3,15):
    print(x,end='\t')

for x in range (1,101,2):
    print(x,end='\t')

print("\n\n#######################\n\n")

sum=0
for x in range(5,9):
     sum=sum+x**2
    
print(sum)

fact =1 
num =3 
for x in range(1,num+1):
    fact = fact * x 

print(f"The factorial of {num} is {fact}")

n=7 
for i in range(2,n):
    if n%i==0:
        print("Not a prime number")
        break
    else:
         print("Prime Number")
         break
# Reverse Number
# ------------------------
rev = 0 
num = 456
n = num 

while num>0:
    digit = num % 10 
    rev = rev * 10 + digit
    num = num // 10 

print(rev) 

#-------------------------
