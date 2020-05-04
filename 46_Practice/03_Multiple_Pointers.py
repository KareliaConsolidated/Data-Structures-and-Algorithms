# Multiple Pointers
# Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition
# Very efficient for solving problems with minimal space complexity as well.

# Write a function called sumZero which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist

############### METHOD 01 : NAIVE SOLUTION ###############

def sumZero(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if (arr[i]+arr[j]) == 0:
				return [arr[i], arr[j]]

############### METHOD 02 ###############

def sumZero(arr):
	left = 0
	right = len(arr)-1
	while left < right:
		arrSum = arr[left] + arr[right]
		if arrSum == 0:
			return [arr[left], arr[right]]
		elif arrSum < 0:
			left += 1
		else:
			right -= 1

print(sumZero([-4, -3, -2, -1, 0, 1, 2, 3, 10])) # [-3, 3]
print(sumZero([-3, -2, -1, 0, 1, 2, 3])) # [-3, 3]
print(sumZero([-2, 0, 1, 3])) # None
print(sumZero([1, 2, 3])) # None			