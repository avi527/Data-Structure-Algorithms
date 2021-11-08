#Program for array rotation
def leftRotate(arr, d, n):
	for rotate in range(d):
		leftRotatebyOne(arr, n)

def leftRotatebyOne(arr,n):
	temp = arr[0]
	for shift in range(n-1):
		arr[shift] = arr[shift+1]
	arr[n-1] = temp

def printArray(size,arr):
	for i in range(size):
		print ("% d"% arr[i], end =" ")

arr = [1,2,3,4,5,6,7]
n = 7
d = 2
leftRotate(arr,d,n)
printArray(n,arr)