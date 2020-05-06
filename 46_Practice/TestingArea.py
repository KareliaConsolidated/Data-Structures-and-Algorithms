def maxSubarraySum(arr, num):
	if len(arr) < num: return None

	maxSum = 0
	tempSum = 0

	for i in range(num):
		maxSum += arr[i]

	tempSum = maxSum

	for j in range(num, len(arr)):
		tempSum = tempSum - arr[j-num] + arr[j]
		maxSum = max(tempSum, maxSum)
	return maxSum

print(maxSubarraySum([2,6,9,2,1,8,5,6,3],3)) # 19
print(maxSubarraySum([1,2,5,2,8,1,5],4)) # 17
print(maxSubarraySum([4,2,1,6],1)) # 6
print(maxSubarraySum([4,2,1,6,2],4)) # 13
print(maxSubarraySum([],4)) # None