def binarySearchAlgo(arr,low,high,x):
	mid= (low+high) // 2
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return binarySearchAlgo(arr,low,mid-1,x)
	else:
		return binarySearchAlgo(arr,mid+1,high,x)
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
high=len(arr)
low=0
aa=binarySearchAlgo(arr,low,high,x)
print(arr[aa])


#Question
#search more than one value index number
def binaryAlgo(arr,low,high,x):
	mid = (low+high) // 2
	if arr1[mid] == x :
		return mid
	elif arr1[mid] > x:
		return binaryAlgo(arr,low,mid-1,x)
	elif arr1[mid] < x:
		return binaryAlgo(arr,mid+1,high,x)
	else:
		print("sorry not match input value")
		
arr1=[3,5,7,9,15,30,48]
x=30
y=9
low=0
high=len(arr1)
bb=binaryAlgo(arr,low,high,x)
cc=binaryAlgo(arr,low,high,y)
print("index is",bb,"value is",arr1[bb])
print("index is",cc,"value is",arr1[cc])

#Question
# Recursive Binary Search Using Iterative
def binarySearch(arr,x):
	low=0
	high=len(arr) -1
	mid=0
	while low <= high:
		mid=(high+low) // 2
		if arr[mid] < x:
			low=mid+1
		elif arr[mid] > x:
			high=mid-1
		else:
			return mid
arr=[3,5,7,9,15,30,48]
x=15
d=binarySearch(arr,x)
print("index is",d,"value is",arr1[d])



