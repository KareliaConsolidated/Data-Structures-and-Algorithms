def QuickSort(arr):
	if len(arr) < 2: return arr

	currentPos = 0

	for i in range(1, len(arr)):
		if arr[i] <= arr[0]:
			currentPos += 1
			arr[i], arr[currentPos] = arr[currentPos], arr[i]
	arr[0], arr[currentPos] = arr[currentPos], arr[0]

	left = QuickSort(arr[:currentPos])

	right = QuickSort(arr[currentPos+1:])

	return left + [arr[currentPos]] + right