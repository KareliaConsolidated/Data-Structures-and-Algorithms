def productofarray(arr):
	if len(arr) == 0:
		return 1
	return arr[0] * productofarray(arr[1:])
