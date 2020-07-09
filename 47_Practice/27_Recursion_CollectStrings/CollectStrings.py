# Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a type of string.
def collectstrings(obj, strcollect = []):
	for key in list(obj.keys()):
		if isinstance(obj[key], dict):
			collectstrings(obj[key], strcollect)
		elif isinstance(obj[key], str):
			strcollect.append(obj[key])
	return strcollect