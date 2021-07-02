# ---------------------- PROBLEM ----------------------------------#
# Write a function called same, which accepts two arrays. The function should 
# return true if every value in the array has it's corresponding value squared 
# in the second array. The frequncy of values must be the same

# Sample input: [1, 2, 3], [1, 9, 4]
# Sample output: True

# ----------------METHOD 01---------------------#

def same(arr1, arr2):
	# Check the length of both array
	if len(arr1) != len(arr2): return False

	# Iterate over each element in array1
	for num in arr1:
		# if element's squared value is not in array2 return False
		if num**2 not in arr2:
			return False
		# else remove that element from array 2
		else:
			arr2.remove(num**2)
	# if all conditions passed, return True
	return True

# ----------------METHOD 02---------------------#

def same_ver_01(arr1, arr2):
	if len(arr1) != len(arr2):
		return False

	return sorted(arr2) == sorted([num**2 for num in arr1])

print(same([1,2,3],[1,4,4]))
print(same([1,2,3],[1,4,9]))
print(same_ver_01([1,2,3],[1,4,4]))
print(same_ver_01([1,2,3],[1,4,9]))