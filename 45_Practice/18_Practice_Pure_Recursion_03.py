# Pure Recursion
# Python program to print odd numbers in a List 

def collectOddValues(arr):
	result = []

	if len(arr) == 0:
		return result

	if arr[0] % 2 != 0:
		result.append(arr[0])

	result = result + collectOddValues(arr[1:])

	return result

print(collectOddValues([1,2,3,4,5,6,7,8,9])) # [1, 3, 5, 7, 9]