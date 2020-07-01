# Divide and Conquer
# This pattern involves dividing a data set into smaller chunks and then repeating a process with a subset of data.
# This pattern can tremendously decrease time complexity.

# Example
# Given a sorted array of integers, write a function called search, that accepts a value and returns the index where the value passed to the function is located. If the value is not found. Return -1

############### METHOD 01 ###############

def binarysearch(arr, val):
	if len(arr) == 0: return -1

	for i in range(len(arr)):
		if arr[i] == val:
			return i
	return -1

############### METHOD 02 ###############

def binarysearch(arr, val):
	start = 0
	end = len(arr) - 1
	while start <= end:
		middle = (start + end) // 2
		if arr[middle] < val:
			start = middle + 1
		elif arr[middle] > val:
			end = middle - 1
		else:
			return middle
	return -1