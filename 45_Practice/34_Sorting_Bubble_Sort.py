def bubble_sort(arr):
	noSwaps = True
	for i in range(len(arr),0,-1):
		for j in range(i-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				noSwaps = False
		if noSwaps == True:
			break
	return arr
	
print(bubble_sort([37,45,29,8])) # 8,29,37,45
print(bubble_sort([8,29,37,45])) # 8,29,37,45