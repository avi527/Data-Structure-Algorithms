# write a python program to remove the array element present immediaately to the right of the element
# entered by the user
def remove_right(input_list,element):
	try:
		index_element = input_list.index(element)
		#Raise execution if element is not in list
	except ValueError:
		print("Element is not present in list")
		return input_list
	if index_element != len(input_list)-1:
		input_list.pop(index_element+1)
	else:
		print("Element is the last one in list")
	return input_list
list_pooped = remove_right([1,2,3,4],2)
for i in list_pooped:
	print(i)