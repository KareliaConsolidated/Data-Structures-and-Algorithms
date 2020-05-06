# Divide and Conquer
# This pattern involves dividing a data set into smaller chunks and then repeating a process with a subset of data.
# This pattern can tremendously decrease time complexity.

# Example
# Given a sorted array of integers, write a function called search, that accepts a value and returns the index where the value passed to the function is located. If the value is not found. Return -1

############### METHOD 01 ###############

def search(arr, val):
	for i in range(len(arr)):
		if arr[i] == num:
			return i
	return -1

############### METHOD 02 ###############
# Time Complexity - Log(N) - Binary Search

def search(arr, val):
	start = 0
	end = len(arr) - 1

	while start <= end:
		middle = ((start + end)//2) 
		if arr[middle] < val:
			start = middle + 1
		elif arr[middle] > val:
			end = middle - 1
		else:
			return middle
	return -1

print(search([1,2,3,4,5,6], 4)) # 3
print(search([1,2,3,4,5,6], 6)) # 5
print(search([1,2,3,4,5,6], 11)) # -1	