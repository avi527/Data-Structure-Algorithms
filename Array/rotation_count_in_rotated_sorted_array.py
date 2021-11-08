# Find the Rotation Count in Rotated Sorted array
def countRotation(arr,n):
	min = arr[0]
	for i in range(0,n):
		if(min>arr[i]):
			min = arr[i]
			min_index = i
	return min_index

arr = [7, 9, 11, 12, 5]
n = len(arr)
print(countRotation(arr,n))