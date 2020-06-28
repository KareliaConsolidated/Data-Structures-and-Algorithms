# Multiple Pointers
# Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition
# Very efficient for solving problems with minimal space complexity as well.

# Write a function called sumZero which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist

def SumZero(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if (arr[i]+arr[j]) == 0:
				return [arr[i],arr[j]]
	return None


def sumZero(arr)				:
	total = 0
	i = 0
	j = len(arr)-1
	while i < j:
		arrSum = arr[i] + arr[j]
		if arrSum == 0:
			return [arr[i], arr[j]]
		elif arrSum < 0:
			i += 1
		else:
			j -= 1
	return None