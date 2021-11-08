# input arr=[1,2,3,2,4,4,-1]
# write a python programm to remove all the occurrences of duplicate array elements

def removeDuplicateArrayElements(arr):
	duplicate_arr = []
	for i in arr:
		if i not in duplicate_arr:
			duplicate_arr.append(i)
	return duplicate_arr
arr=[1,2,3,2,4,4,-1]
remove_duplicate = removeDuplicateArrayElements(arr)
print(remove_duplicate)