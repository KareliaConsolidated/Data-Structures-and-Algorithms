def search(arr, num):
	if len(arr) == 0: return -1
	
	start = 0
	end = len(arr) - 1

	while start <= end:
		middle  = (start + end) // 2
		if arr[middle] < num:
			start = middle + 1
		elif arr[middle] > num:
			end = middle - 1
		else:
			return middle
	return -1

print(search([1,2,3,4,5,6], 4)) # 3
print(search([1,2,3,4,5,6], 6)) # 5
print(search([1,2,3,4,5,6], 11)) # -1	