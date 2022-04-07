perlist=[
    
]
n= int(input('how many persons: '))
for per in range(0,n): 
    persons={}
    print('Record number:', per+1)
    persons['ID']=per+1  
    persons['name']=input('Enter your Name: ')
    persons['email']=input('Enter your Email: ')    
    perlist.append(persons)

      

print('%-5s %-30s %-20s'% ("ID","Name", "Email" ))
print('='*80)
for per in perlist: 
    print('%-5s %-30s %-20s'% (per["ID"], per["name"], per["email"] ))

