# Reverse Strings
# The Goal is to write a function that takes a string as input and then returns the reversed string.
# For Example, if the input is the string "Bear", then the output should be "raeB"
def string_reverser(string):
	"""
	Reverse the Input String
	Args: String to be Reversed
	Returns: The Reversed String
	"""
	new_rev = []
	for i in range(len(string)):
		new_rev.append(string[-1-i])
	return ''.join(new_rev)
	# return string[::-1] # LOL

# Test Cases
print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")