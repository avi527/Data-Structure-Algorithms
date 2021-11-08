
#check a print number or not
num = 11
if num < 2:
	print(num, "is not prime number")
else:
	for i in range(2,num):
		if(num % i) == 0:
			print(num, "is not prime number")
			break
	else:
		print(num, "is prime number")
print("-------------------------------------------------")
#find prime number b/w 10-100

def listPrimeNumber(s,num):
	for val in range(s,num + 1):  
	   if val > 1:  
	       for i in range(2,val):  
	           if (val % i) == 0:  
	               break  
	       else:  
	           print(val) 
num = 100
listPrimeNumber(10,num)