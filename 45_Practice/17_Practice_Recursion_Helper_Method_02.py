def collectOdds(arr):
	result = []
	def helper(helperInput):
		if len(helperInput) == 0: return

		if helperInput[0] % 2 != 0:
			result.append(helperInput[0]) 
		helper(helperInput[1:])
	helper(arr)
	return result

print(collectOdds([1,2,3,4,5,6,7,8,9]))	# [1, 3, 5, 7, 9]