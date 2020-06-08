#input arr[] = [1, 2, 3, 4, 5, 6, 7]
#output = [3, 4, 5, 6, 7,1, 2]

def arrayRotate(arr,n,d):
	for i in range(d):
		arrayRotateOneByOne(arr,n)
def arrayRotateOneByOne(arr,n):
	temp=arr[0]
	for i in range(n-1):
		arr[i]=arr[i+1]
	arr[n-1]=temp
def printArray(arr,size):
	for i in range(size):
		print(arr[i],end=" ")

arr=[1,2,3,4,5,6,7]
n=len(arr)
d=2
arrayRotate(arr,n,d)
printArray(arr,n)

#python program for reversal algorithum of array rotation
def reverseArray(arr,start,end):
	while (start < end):
		temp=arr[start]
		arr[start]=arr[end]
		arr[end]=temp
		start +=1
		end=end-1
def leftRotatedArray(arr,d):
	if d==0:
		return 
	n=len(arr)
	reverseArray(arr,0,d-1)
	reverseArray(arr,d,n-1)
	reverseArray(arr,0,n-1)
def printArray(arr):
	for i in range(0,len(arr)):
		print(arr[i],"ans")

arr=[1,2,3,4,5,6,7]
n=len(arr)
d=2

leftRotatedArray(arr,d)
printArray(arr)
