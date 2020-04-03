def insertion_sort(arr):
	for i in range(1,len(arr)):
		currentVal = arr[i]

		j = i-1
		while j>=0 and currentVal < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = currentVal
	return arr

print(insertion_sort([13,14,11,12,19,18,17,16,15])) # [11, 12, 13, 14, 15, 16, 17, 18, 19]