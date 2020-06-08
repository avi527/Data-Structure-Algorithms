# Search, insert and delete in a sorted array
'''
In this  search, insert and delete operation in a sorted array is discussed.
'''

#Search Operation

def SearchOperation(arr,l,h,x):
	mid=(l+h) // 2
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return SearchOperation(arr,l,h-1,x)
	elif arr[mid] < x:
		return SearchOperation(arr,l+1,h,x)
	else:
		print("something with wrong")


arr = [5, 6, 7, 8, 9, 10] 
low=0
high=len(arr)
x=10
sO=SearchOperation(arr,low,high,x)
print("index is ", sO,"value is",arr[sO])

print("--------------------------------------------------")

#Insert Operation Sorted Array
def insertSorted(arr,key):
	newarr=[None]*(len(arr)+1)
	for i in range(len(arr)):
		if arr[i] < key:
			newarr[i]=arr[i]
			newarr[i+1]=key
		elif arr[i] > key:
			newarr[i+1]=arr[i]
	#print(newarr)
	for i in range(len(newarr)):
		print(newarr[i],end=" ") 
arr=[10,20,30,40,50]
key=26
insertSorted(arr,key)
print("-----------------------------------------------")

#Insert Operation Unsorted Array
arr = [12, 6, 9, 11, 18, 16]
index=2
val=20
temp=""
narr=[None]*(len(arr)+1)
for i in range(len(arr)):
	if i < index:
		narr[i]=arr[i]
		narr[i+1]=val
	else:
		narr[i+1]=arr[i]
print(narr)

print("-----------------------------------------------")


#Delete Operation Sorted Array
#Search value using reverse Binary searching algo
def binarySearch(arr,val,l,h):
	mid=(l+h) // 2
	if arr[mid] == val:
		return mid
	elif arr[mid] > val:
		return binarySearch(arr,val,l,mid-1)
	elif arr[mid] < val:
		return binarySearch(arr,val,mid+1,h)
	else:
		print("not match !!!")

arr = [10, 20, 30, 40, 50,60,70 ] 
h = len(arr) 
val = 50
bS=binarySearch(arr,val,0,h)
print(arr[bS])
bSearch=arr[bS]
print("----------------------------------------------")

def deleteArray(bS,arr,n):
	temp=[]
	for i in range(n):
		if arr[i] != bs:
			temp=arr[i]
		print(temp)

arr = [10, 20, 30, 40, 50,60,70 ]
n=len(arr)
bs=20 
deleteArray(bS,arr,n)

