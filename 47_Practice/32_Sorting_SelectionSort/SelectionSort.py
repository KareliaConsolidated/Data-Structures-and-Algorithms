def SelectionSort(arr):
	for i in range(len(arr)):
		minIdx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[minIdx]:
				minIdx = j
		arr[i], arr[minIdx] = arr[minIdx], arr[i]
	return arr