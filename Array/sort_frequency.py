# write a python program to sort the array elements in increasing order of ther frequencies
def freq_sort(arr):
	freq = dict()
	for i in range(len(arr)):
		if arr[i] in freq:
			freq[arr[i]] += 1
		else:
			freq[arr[i]] = 1
	return [key for key, value in sorted(freq.items(), key=lambda item: item[1])]

lst = [1,2,3,2,4,4,4]
print(freq_sort(lst))
