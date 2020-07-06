# Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

def flatten(arr):
	if len(arr) == 0: return arr
	if isinstance(arr[0], list):
		return flatten(arr[0]) + flatten(arr[1:])
	return arr[:1] + flatten(arr[1:])
