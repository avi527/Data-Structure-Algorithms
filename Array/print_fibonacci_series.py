num = 2
preval = 0
currentval = 1
for i in range(1,num):
	prevalpreval = preval
	preval = currentval
	currentval = preval+prevalpreval
print(currentval) 
