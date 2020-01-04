# Write a recursive function called someRecursive which accepts an array and a callback. The function returns True if a single value in the array returns True when passed to the callback. Otherwise it returns False.
def isOdd(val):
	if val % 2 != 0:
		return True
	return False

def isEven(val):
	if val % 2 == 0:
		return True
	return False

def someRecursive(arr,f):
	if len(arr) == 0: return False
	if f(arr[0]): return True
	return someRecursive(arr[1:], f)

print(someRecursive([2,3,4], isOdd)) # True
print(someRecursive([2,4,6,8], isEven)) # True