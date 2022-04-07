for row in range(5):
    for col in range (6):
        print(col,end=" ")

    print('\r')    


for row in range(10):
    for col in range (0,10-row):
        print(col,end=" ")

    print('\r') 

def pypart(n):
    mylist = []
    for i in range(1,n+1):
        mylist.append(str(i)*i)
    print("\n".join(mylist))

# Driver Code
n = 5 
pypart(n)  

# Python code 3.x to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def contalpha(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
    num = 65

	# outer loop to handle number of rows
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
		
			# printing char value
            print(ch, end=" ")
    
			# incrementing at each column
            num = num +1
	
	
		# ending line after each row
        print("\r")

# Driver code
n = 5
contalpha(n)
