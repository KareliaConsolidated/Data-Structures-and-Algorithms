# Write a recursive function called capitalizeWords. Given array of words, return a new array containing each word capitalized.

################# METHOD 01 #################

def capitalizeWords(arr, result=[]):
	if len(arr) == 0: return result
	result.append(arr[0].upper())
	return capitalizeWords(arr[1:], result)