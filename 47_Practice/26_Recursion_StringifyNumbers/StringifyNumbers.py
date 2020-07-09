# Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and convert them to strings. 
def stringifyNumbers(obj):
	
	for key in list(obj.keys()):
		if len(obj) == 0: return obj

		if type(obj[key]) == dict:
			stringifyNumbers(obj[key])
		elif type(obj[key]) == int:
			obj[key] = str(obj[key])
			
	return obj