############ METHOD 01 ##############

def linearSearch(arr, val):
	for idx, num in enumerate(arr):
		if num == val:
			return idx
	return -1

############ METHOD 02 ##############

def linearSearch(arr, val):
	return arr.index(val) if val in arr else -1

print(linearSearch([34,51,1,2,3,45,56,687], 45)) # 5
print(linearSearch([34,51,1,2,3,45,56,687], 100)) # -1