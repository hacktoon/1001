
def binary_search(value, l):
	if len(l) == 0:
		return -1
	mid = len(l)/2
	if value < l[mid]:
		return binary_search(value, l[:mid])
	elif value > l[mid]:
		tmp = binary_search(value, l[(mid + 1):])
		return (-1 if tmp == -1 else tmp + mid + 1)
	else:
		return mid
