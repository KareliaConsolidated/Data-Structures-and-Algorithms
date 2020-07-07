# Write a recursive function called NestedEvenSum. Return the sum of all even numbers in an object which may contain nested objects

def NestedEvenSum(obj, evensum = 0):
	for key in list(obj.keys()):
		if isinstance(obj[key], dict):
			evensum += NestedEvenSum(obj[key])
		elif (isinstance(obj[key], int) and (obj[key] % 2 == 0)):
			evensum += obj[key]
	return evensum