# write a python program to find the frequency of each element in array A
def findFrequency(a):
	frequency = {}
	for num in a:
		if num in frequency.keys():
			frequency[num] += 1
		else:
			frequency[num] =1
	return frequency

frequency = findFrequency([1,2,3,4,5,5,4,3,2,1,7,8])
for keys,values in frequency.items():
	print(keys,"--",values)