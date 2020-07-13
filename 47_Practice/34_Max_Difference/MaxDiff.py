def MaxDiff(arr):
	i_idx = 0
	j_idx = 0
	max_Diff = float('-inf')
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if abs(arr[j] - arr[i]) > max_Diff:
				max_Diff = abs(arr[j] - arr[i])
				i_idx = i
				j_idx = j
	return max_Diff, (j_idx, i_idx)

print(MaxDiff([12,45,56,14,2]))
print(MaxDiff([]))

