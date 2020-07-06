# Write a function called someRecursive which accepts an array and a callback. The function returns true if a single value in the array returns true when passed to the call back. Otherwise it returns False.
def isOdd(num):
	if num % 2 != 0: return True

def isEven(num):
	if num % 2 == 0: return True

def someRecursive(arr, fun):
	if len(arr) == 0: return False
	if fun(arr[0]): return True
	return someRecursive(arr[1:], fun)