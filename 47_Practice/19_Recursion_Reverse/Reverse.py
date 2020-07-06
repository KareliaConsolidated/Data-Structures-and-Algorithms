# Write a recursive function called reverse which accepts a string and returns a new string in reverse

def reverse(string):
	if len(string) <= 0: return string
	return reverse(string[1:]) + string[0]