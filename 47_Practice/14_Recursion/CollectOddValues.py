############# METHOD 01 #############
def CollectOddValues(arr):
	OddArray = []

	def helper(helperInput):
		if len(helperInput) == 0: return []

		if helperInput[0] % 2 != 0:
			OddArray.append(helperInput[0])

		helper(helperInput[1:])

	helper(arr)

	return OddArray

print(CollectOddValues([1,2,3,4,5,6]))	

############# METHOD 02 #############

def CollectOddNums(arr, result = []):
	if len(arr) == 0: return result

	if arr[0] % 2 != 0:
		result.append(arr[0])

	return CollectOddNums(arr[1:], result)

print(CollectOddNums([1,2,3,4,5,6]))	