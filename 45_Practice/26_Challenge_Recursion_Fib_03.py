# Write a recursive function called someRecursive which accepts an array and a callback. The function returns True if a single value in the array returns True when passed to the callback. Otherwise it returns False.
def isOdd(num):
	if num % 2 != 0: return True
	return False

def isEven(num):
	if num % 2 != 0: return False
	return True

def someRecursive(arr,clbk):
	if len(arr) == 0: return False
	if clbk(arr[0]): return True
	return someRecursive(arr[1:],clbk)

print(someRecursive([2,3,4], isOdd)) # True
print(someRecursive([2,4,6,8], isEven)) # True