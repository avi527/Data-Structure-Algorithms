# write a python program to remove the array element with maximum frequency
def getFrequency(a):
	frequency = {}
	for num in a:
		if num not in frequency.keys():
			frequency[num] = 1
		else:
			frequency[num] += 1
	return frequency
#frequency = getFrequency([1,2,3,4,5,5,4,3,2,1,7,8])

def removeElement(input_data):
	count_frequency = getFrequency(input_data)
	element = -1
	max_frequency = 0
	frequency = {}
	for val in count_frequency.keys():
		if max_frequency < count_frequency[val]:
			max_frequency = count_frequency[val]
			element = val
	for i in range(max_frequency):
		input_data.remove(element)
	return input_data
frequency = [1,2,2,12,2,12,121,212]
result = removeElement(frequency)
print(result)