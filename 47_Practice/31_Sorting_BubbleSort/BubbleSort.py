def BubbleSort(arr):
	Swap = False
	for i in range(len(arr),0,-1):
		for j in range(i-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				Swap = True
		if Swap == False:
			break
	return arr

print(BubbleSort([8,1,2,3,4,5,6,7])) # [1, 2, 3, 4, 5, 6, 7, 8]
print(BubbleSort([5,4,3,1,2])) # [1,2,3,4,5]
print(BubbleSort([])) # []
print(BubbleSort([5,4,3,1,2,-6])) # [-6, 1, 2, 3, 4, 5]