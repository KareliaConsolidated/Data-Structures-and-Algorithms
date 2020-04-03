def selection_sort(arr):
	for i in range(len(arr)):
		lowest = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[lowest]:
				lowest = j
		temp = arr[i]
		arr[i] = arr[lowest]
		arr[lowest] = temp
	return arr

print(selection_sort([34,22,12,10,8,42,17]))