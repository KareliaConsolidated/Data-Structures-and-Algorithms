def MergeHelper(arr1, arr2):
	i = 0
	j = 0
	NewArr = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			NewArr.append(arr1[i])
			i += 1
		else:
			NewArr.append(arr2[j])
			j += 1

	if j < len(arr2):
		NewArr += arr2[j:]
	elif i < len(arr1):
		NewArr += arr1[i:]

	return NewArr

def MergeSort(arr):
	if len(arr) <= 1: return arr
	mid = len(arr) // 2
	FirstArr, SecondArr = MergeSort(arr[:mid]), MergeSort(arr[mid:])
	return MergeHelper(FirstArr, SecondArr)

print(MergeSort([5,4,3,1,2]))

