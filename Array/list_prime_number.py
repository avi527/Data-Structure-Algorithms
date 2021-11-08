# write a python program to create a list of all prime number
def listPrimeNumber(num):
	for val in range(0,num + 1):  
	   if val > 1:  
	       for i in range(2,val):  
	           if (val % i) == 0:  
	               break  
	       else:  
	           print(val) 
num = 100
listPrimeNumber(num)
