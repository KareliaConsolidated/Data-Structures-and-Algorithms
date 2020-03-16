# Write a recursive function called capitalizeWords. Given array of words, return a new array containing each word capitalized.

################# METHOD 01 #################

def capitalizeWords(arr, result=[]):
	if len(arr) == 0: return result
	result.append(arr[0].upper())
	return capitalizeWords(arr[1:], result)

################# METHOD 02 #################

def capitalizeWords(arr):
	result = []

	def helper(helperInput):
		if len(helperInput) == 0: return None
		result.append(helperInput[0].upper())
		helper(helperInput[1:])

	helper(arr)

	return result

print(capitalizeWords(['i','am','learning','data','science'])) # ['I', 'AM', 'LEARNING', 'DATA', 'SCIENCE']


