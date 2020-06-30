# ---------------------- PROBLEM 08 (RANDOM) ----------------------------------#
# Write a function called minSubarrayLen which accepts two parameters - an array
# of positive integers and a positive integer. The function should return the minimum
# length of a contigous subarray of which the sum is greater than or equal to the integer
# passed to the function. If there isn't one, return 0 instead.

# Sample input: [2, 3, 1, 2, 4, 3], 7
# Sample output: 2

# ----------------METHOD 01---------------------#

def MinSubArrayLen(arr, target):
	if len(arr) == 0: return 0

	minLen = float('inf')

	for i in range(len(arr)):
		total = 0
		j = i
		while j < len(arr):
			total += arr[j]
			if total >= target:
				minLen = min(minLen, j-i+1)
				break
			j += 1
	return minLen if minLen != float('inf') else 0

# ----------------METHOD 02---------------------#

def minSubArrayLen(arr, num):
	total = 0
	minLength = float('inf')
	left = 0
	for right, val in enumerate(arr):
		total += val
		while total >= num:
			minLength = min(minLength, right-left+1)
			total -= arr[left]
			left += 1
	return minLength if minLength <= len(arr) else 0	

# ----------------METHOD 03---------------------#

# COMPLEXITY = TIME: O(n), SPACE: O(1)
def minSubarrayLen(arr, target):
	# define variables
	start = 0
	end = 0 
	total = 0 
	minSubLen = float("inf")

	# iterate over array
	while start < len(arr):
		# check if we have reached target, if not keep adding numbers
		if (total < target) and (end < len(arr)):
			total += arr[end]
			end += 1
		# if total is greater than the target, compare with minLen
		elif total >= target:
			minSubLen = min(minSubLen, end - start)
			total -= arr[start]
			start += 1
		# else break out of loop
		else:
			break
	return minSubLen if minSubLen != float("inf") else 0

# ----------------METHOD 03---------------------#	