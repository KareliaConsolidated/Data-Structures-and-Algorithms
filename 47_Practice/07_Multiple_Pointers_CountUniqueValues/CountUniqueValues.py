# ---------------------- PROBLEM 07 (RANDOM) ----------------------------------#
# Implement a function called countUniqueValues which accepts a sorted array, and
# counts the unique values in the array. There can be negative numbers in the
# array, but it will always be sorted.

# Assumption: The numbers in array are always sorted

# Sample input: [1, 1, 1, 1, 1, 2]
# Sample output: 2

# ----------------METHOD 01---------------------#
def CountUniqueValues(arr):
	if len(arr) == 0: return None

	ptr_1 = 0

	for ptr_2 in range(1, len(arr)):
		num1, num2 = arr[ptr_1], arr[ptr_2]
		if num1 != num2:
			ptr_1 += 1
			arr[ptr_1] = num2
	return ptr_1 + 1

# ----------------METHOD 02---------------------#
def CountUniqueValues(arr):
	if len(arr) == 0: return None

	num = arr[0]
	count = 1

	for ptr_2 in range(1, len(arr)):
		Currnum = arr[ptr_2]
		if Currnum != num:
			count += 1
			num = Currnum
	return count

# ----------------METHOD 03---------------------#	
def CountUniqueValues(arr):
	if len(arr) == 0: return None
	return len(set(arr))