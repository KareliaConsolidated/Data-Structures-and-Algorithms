# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns False
def isPalindrome(string):
	if len(string) == 0: return False
	if len(string) == 1: return True
	if len(string) == 2: return string[0] == string[1]
	if string[0] == string[-1]:
		return isPalindrome(string[1:-1])
	else:
		return False