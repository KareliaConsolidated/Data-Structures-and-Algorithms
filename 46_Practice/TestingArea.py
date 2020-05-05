def same(arr1,arr2):
	if len(arr1) != len(arr2):
		return False
	
	squared_count = {num:arr2.count(num) for num in arr2}

	for i in range(len(arr1)):
		value_count = arr1.count(arr1[i])
		if squared_count[arr1[i]**2] != value_count:
			return False
	return True

print(same([1,2,3],[4,1,9])) # True
print(same([1,2,3],[1,9])) # False
print(same([1,2,1],[4,4,1])) # False