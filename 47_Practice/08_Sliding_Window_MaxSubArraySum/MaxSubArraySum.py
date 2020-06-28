# ---------------------- PROBLEM 08 (RANDOM) ----------------------------------#
# Write a function called maxSubarraySum which accepts an array of integers and
# a number called n. The function should calculate the maximum sum of n consecutive 
# elements in the array.

# Sample input: [1, 2, 5, 2, 8, 1, 5], 2
# Sample output: 10

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
def MaxSubArraySum(arr, num):
	# Check Length of Array, if its less than num than return None
	if len(arr) < num: return None
	# Define maxSum = -inf, to compare with the maxSum
	maxSum = float('-inf')
	# Initiate For Loop to iterate over arr starting from i to i+num
	for i in range((len(arr)-num)+1):
		# Sum Four Elements of an array
		numSum = sum(arr[i:i+num])
		# Compare it with maxSum
		if maxSum < numSum:
			# if Sum is greater than maxSum, replace the value of sum with maxSum
			maxSum = numSum
	# Return maxSum
	return maxSum

# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def MaxSubArraySum(arr, num):
	if len(arr) < num: return None
	
	SubArraySum = sum(arr[0:num])
	
	MaxSum = SubArraySum

	for end in range(num, len(arr)):
		SubArraySum = SubArraySum + arr[end] - arr[end-num]
		MaxSum = max(MaxSum, SubArraySum)
	return MaxSum