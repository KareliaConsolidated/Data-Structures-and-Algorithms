# Sliding Window - maxSubarraySum
# Given an array of integers and a number, write a function called maxSubarraySum which finds the maximum sum of a subarray with the length of the number passed to the function.

# Note that a subarray must consist of consecutive elements from the original array. In the first example below, [100,200,300] is a subarray of the original array, but [100,300] is not.

def maxSubarraySum(arr,num):
	maxSum = 0
	tempSum = 0

	if len(arr) < num: return None

	for i in range(num):
		maxSum += arr[i]

	tempSum = maxSum

	for j in range(num, len(arr)):
		tempSum = tempSum - arr[j-num] + arr[j]
		if tempSum > maxSum:
			maxSum = tempSum
	return maxSum

print(maxSubarraySum([100,200,300,400], 2)) # 700
print(maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)) # 39
print(maxSubarraySum([-3,40,-2,6,-1], 2)) # 5
print(maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1], 2)) # 5
print(maxSubarraySum([2,3], 3)) # None