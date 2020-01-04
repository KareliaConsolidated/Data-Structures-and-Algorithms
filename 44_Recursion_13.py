# Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

################# METHOD 01 #################

def capitalizeFirst(arr):
	result = []

	def helper(helperInput):
		if len(helperInput) == 0:
			return None
		result.append(helperInput[0].capitalize())
		helper(helperInput[1:])

	helper(arr)
	return result

################# METHOD 02 #################
def capitalizeFirst(lst, result = []):
	if len(lst) == 0:
		return result
	result.append(lst[0].capitalize())
	return capitalizeFirst(lst[1:], result)

print(capitalizeFirst(['car','taco','tacocat','banana'])) # ['Car', 'Taco', 'Tacocat', 'Banana']