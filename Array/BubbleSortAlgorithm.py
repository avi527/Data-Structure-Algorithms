'''
Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly 
swapping the adjacent elements if they are in wrong order.
'''

#Question Bubble Sort Algo using non-linear(Loop)
def bubbleSort(arr):
	n=len(arr)
	for i in range(0,n):
		for j in range(0,n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
for i in range(len(arr)): 
    print ("%d" %arr[i]),  

#Bubble sorting using Recursion Method

def sortBubbleRecursion(arr):
	for i,num in enumerate(arr):
		try:
			if arr[i+1] < num:
				arr[i] = arr[i+1]
				arr[i+1] = num
				sortBubbleRecursion(arr)
		except IndexError:
			pass
	return arr

arr=[60, 31, 21, 11, 22, 12, 90] 
sortBubbleRecursion(arr)
for i in arr:
	print(i,end=" ")
