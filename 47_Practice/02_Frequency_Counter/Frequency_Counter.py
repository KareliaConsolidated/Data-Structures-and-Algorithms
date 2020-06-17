# Write a function called same, which accepts two arrays. The function should return True, if every value in the array has its corresponding value squared in the second array. The frequency of values must be the same.
########### METHOD 01 ##############
def same(arr1, arr2):
	if len(arr1) != len(arr2):
		return False

	squared_dict = {}

	for i in range(len(arr2)):
		if arr2[i] in squared_dict:
			squared_dict[arr2[i]] += 1
		else:
			squared_dict[arr2[i]] = 1

	for j in range(len(arr1)):
		val_count = arr1.count(arr1[j])
		if squared_dict[arr1[j]**2] != val_count:
			return False
	return True

########### METHOD 02 ##############
# def same(arr1, arr2):
# 	if len(arr1) != len(arr2):
# 		return False
# 	return sorted([val**2 for val in arr1]) == sorted(arr2)