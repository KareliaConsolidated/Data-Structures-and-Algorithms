# Capitalize First
# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

################ Method 01 ################

def capitalizefirst(arr, result=[]):
	if len(arr) == 0: return result
	result.append(arr[0].capitalize())
	return capitalizefirst(arr[1:], result)

################ Method 02 ################

def capitalizefirst(arr):

	result = []

	def helper(helperInput):
		if len(helperInput) == 0: return None
		result.append(helperInput[0].capitalize())
		helper(helperInput[1:])

	helper(arr)

	return result

################ Method 03 ################

def capitalizefirst(arr):
	if len(arr) == 0: return arr
	return [arr[0].title()] + capitalizefirst(arr[1:])