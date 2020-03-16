# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

################# METHOD 01 #################

def capitalizeFirst(arr, result=[]):
	if len(arr) == 0: return result
	result.append(arr[0].capitalize())
	return capitalizeFirst(arr[1:], result)

################# METHOD 02 #################

def capitalizeFirst(arr):
	result = []

	def helper(helperInput):
		if len(helperInput) == 0: return None
		result.append(helperInput[0].capitalize())
		helper(helperInput[1:])

	helper(arr)

	return result

print(capitalizeFirst(['car','taco','tacocat','banana'])) # ['Car', 'Taco', 'Tacocat', 'Banana']