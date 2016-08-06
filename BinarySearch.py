def binarySearch(sequence, number, lower, upper):
	if upper == lower:
		assert number == sequence[upper]
		return upper
	else:
		mid = (upper+lower)//2
		if number > sequence[mid]:
			return binarySearch(sequence, number, mid + 1, upper)
		else : 
			return binarySearch(sequence, number, lower, mid)