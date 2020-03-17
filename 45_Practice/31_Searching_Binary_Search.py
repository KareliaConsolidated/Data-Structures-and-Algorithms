def BinarySearch(arr,num):
	start = 0
	end = len(arr)-1
	middle = (start + end )//2
	while start <= end:

		if num > middle:
			start = middle + 1
		else:
			end = middle - 1
		
		middle = (start + end) // 2

		if arr[middle] == num:
			return middle
	return -1

numarray = [1,2,3,4,5,6,7,8,9,10]

print(BinarySearch(numarray,2))