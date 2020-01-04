# Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

def flatten(arrs):
	if arrs == []:
		return arrs
	if isinstance(arrs[0], list):
		return flatten(arrs[0]) + flatten(arrs[1:])
	return arrs[:1] + flatten(arrs[1:])

print(flatten([1,2,3,[4,5]])) # [1,2,3,4,5]
print(flatten([1,[2,3,[4,[5]]]])) # [1,2,3,4,5]