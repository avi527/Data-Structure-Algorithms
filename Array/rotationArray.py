def LeftRotate(arr,d,n):
	for i in range(d):
		leftRotateByOne(arr,n)
def leftRotateByOne(arr,n):
	temp=arr[0]
	for i in range(n-1):
		arr[i] = arr[i+1]
	print(arr[n-1])
	arr[n-1] = temp

def printArray(arr,size):
	for i in range(size):
		print(arr[i],end=" ")


arr=[1,2,3,4,5,6,7]
d=2
n=6
LeftRotate(arr,d,n)
#printArray(arr,n)


'Remote_Download_Status', '[{\"lookupId\": \"RDSASS\", \"lookupType\": \"Remote_Download_Status\", \"lookupValue\": \"Assigned\"}, {\"lookupId\": \"RDSCOM\", \"lookupType\": \"Remote_Download_Status\", \"lookupValue\": \"Completed\"}, {\"lookupId\": \"RDSPRO\", \"lookupType\": \"Remote_Download_Status\", \"lookupValue\": \"In Progress\"}, {\"lookupId\": \"RDSREV\", \"lookupType\": \"Remote_Download_Status\", \"lookupValue\": \"In Review\"}]'
