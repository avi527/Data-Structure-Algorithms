# write a python program to copy the element of array A to B
def copyArray(a):
	b = [None] * len(a)
	for i in range(0,len(a)):
		b[i] = a[i]
	print(b)

a=[5,6,3,4,8,9]
copyArrayOtherWay(a)