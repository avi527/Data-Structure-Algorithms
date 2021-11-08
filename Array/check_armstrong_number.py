n = 407
num = n
sum = 0
order = len(str(n))
while(n>0):
	digit = n % 10
	sum += digit ** order
	n = n // 100
if sum == num:
	print(num,"is armstrong number")
else:
	print(num, "is not armstrong number") 
