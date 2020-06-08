'''
1) Find middle point mid = (l + h)/2
2) If key is present at middle point, return mid.
3) Else If arr[l..mid] is sorted
    a) If key to be searched lies in range from arr[l]
       to arr[mid], recur for arr[l..mid].
    b) Else recur for arr[mid+1..h]
4) Else (arr[mid+1..h] must be sorted)
    a) If key to be searched lies in range from arr[mid+1]
       to arr[h], recur for arr[mid+1..h].
    b) Else recur for arr[l..mid]
'''

#Questions:
# Search an element in sorted and rotated array using 
# single pass of Binary Search 
def search(arr,l,h,key):
	mid=(l+h) // 2
	if arr[mid] == key:
		return mid
	if arr[l] <= arr[mid]:
		if key >= arr[l] and key <= arr[mid]:
			return search(arr, l, mid-1, key)
		return search(arr, mid+1, h, key)

	if key >= arr[mid] and key <= arr[h]:
		return search(a, mid+1, h, key)
	return search(arr, l, mid-1, key) 
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 6
h=len(arr)
l=0
s=search(arr,l,h,key)
print(s)
