def pairInSortedRotated(arr,s,n):
	temp = arr[0]
	l = []
	for i in range(n):
		for j in range(1,n):
			l = arr[i]+arr[j]
		if s == l:
			print("1st element is",arr[i],"and second element is",arr[j],"sum of both element is",l)

s = 16
arr = [11,15,6,8,9,10]
n = len(arr)
pairInSortedRotated(arr,s,n)