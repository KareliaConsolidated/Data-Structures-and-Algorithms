# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.
def capitalizeFirst(arr):
	result = []

	def helper(helperInput):
		if len(helperInput) == 0:
			return None
		result.append(helperInput[0].capitalize())
		helper(helperInput[1:])

	helper(arr)
	return result

print(capitalizeFirst(['car','taco','tacocat','banana']))