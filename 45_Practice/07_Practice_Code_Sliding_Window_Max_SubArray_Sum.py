# Sliding Window
# This pattern involves creating a window which can either be array or number from one position to another.
# Depending on a certain condition, the windows either increases or closes (and a new window is created)
# Very useful for keeping track of a subset of data in an array/string etc

# Example
# Write a function called maxSubarraySum which accepts an array of integers and a number called n. The function should calculate the maximum sum of n consecutive elements in the array.

def maxSubarraySum(arr, num):
	if len(arr) < num: return None
	maxSum = 0
	tempSum = 0

	for i in range(num):
		maxSum += arr[i]

	tempSum = maxSum

	for j in range(num, len(arr)):
		tempSum = tempSum - arr[j - num] + arr[j]
		maxSum = max(tempSum, maxSum)
	
	return maxSum		

print(maxSubarraySum([2,6,9,2,1,8,5,6,3],3)) # 19
print(maxSubarraySum([1,2,5,2,8,1,5],4)) # 17
print(maxSubarraySum([4,2,1,6],1)) # 6
print(maxSubarraySum([4,2,1,6,2],4)) # 13
print(maxSubarraySum([],4)) # None