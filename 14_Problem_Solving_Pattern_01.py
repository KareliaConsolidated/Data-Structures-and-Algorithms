# Frequency Counter
# Example: Write a function called same, which accepts two arrays. The function should return true if every value in the array has its corresponding value squared in the second array. The frequency of values must be the same.
############### METHOD 01 ###############

def same(arr1, arr2):
	squared_dict = {}
	if len(arr1) != len(arr2):
		return False

	for i in range(len(arr2)):
		if i in squared_dict:
			squared_dict[arr2[i]] += 1
		else:
			squared_dict[arr2[i]] = 1
	
	for num in arr1:
		cot = arr1.count(num)
		if squared_dict[num**2] != cot:
			return False
	return True

############### METHOD 02 ###############

def same(arr1, arr2):
	if len(arr1) != len(arr2):
		return False
	return sorted([num**2 for num in arr1]) == sorted(arr2)

print(same([1,2,3],[4,1,9])) # True
print(same([1,2,3],[1,9])) # False
print(same([1,2,1],[4,4,1])) # False