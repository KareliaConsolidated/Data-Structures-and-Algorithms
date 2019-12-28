# Sliding Window - minSubArrayLen
# Write a function called minSubArrayLen which accepts two parameters - an array of positive integers and a positive integer.
# This function should return the minimal length of contiguous subarray of which the sum is greater than or equal to the integer passed to the function. If there isn't one, return  0 instead.

def minSubArrayLen(arr, su):
	total = 0
	left = 0
	minLength = float('inf')
	for right,val in enumerate(arr):
		total += val
		while total >= su:
			minLength = min(minLength, right-left+1)
			total -= arr[left]
			left += 1
	return minLength if minLength <= len(arr) else 0

print(minSubArrayLen([1,1,1],3))
print(minSubArrayLen([2,3,1,2,4,3], 7)) # 2
print(minSubArrayLen([2,1,6,5,4], 9)) # 2 
print(minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52)) # 1
print(minSubArrayLen([1,4,16,22,5,7,8,9,10], 39)) # 3
print(minSubArrayLen([1,4,16,22,5,7,8,9,10], 55)) # 5
print(minSubArrayLen([4, 3, 3,8, 1, 2,3], 11)) # 2
print(minSubArrayLen([1,4,16,22,5,7,8,9,10], 95)) # 0
