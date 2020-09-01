def countZeros(arr):
	left = 0
	right = len(arr) - 1
	
	if arr[left] == 1 and arr[right] == 1: return 0
	if arr[left] == 0 and arr[right] == 0: return len(arr)

	while left < right:
		mid = (left + right) // 2
		if arr[mid] == 1:
			left = mid + 1
		elif arr[mid] == 0:
			right = mid
	return len(arr) - right

print(countZeros([1,1,0,0,0,0,0,0]))
print(countZeros([1,1,1,1,0,0]))
print(countZeros([1,0,0,0,0]))
print(countZeros([1,1,1,1]))
print(countZeros([0, 0]))
print(countZeros([1,1,1,1,0]))