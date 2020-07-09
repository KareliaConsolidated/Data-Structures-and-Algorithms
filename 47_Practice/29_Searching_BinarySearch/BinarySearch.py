def BinarySearch(arr, num):
	start = 0
	end = len(arr)-1
	while start <= end:
		middle = (start + end)//2
		middlenum = arr[middle]
		if middlenum > num:
			end = middle - 1 
		elif middlenum < num:
			start = middle + 1
		else:
			return middle
	return -1 
	
numarray = [1,2,3,4,5,6,7,8,9,10]
print(BinarySearch(numarray,11)) # -1
print(BinarySearch(numarray,3)) # 2
