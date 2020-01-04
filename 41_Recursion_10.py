# Write a recursive function called isPalindrome which returns True if the string passed to it is a palindrome (reads the same forward and backward), Otherwise its False.
def isPalindrome(stri):
	if len(stri) == 1: return True
	if len(stri) == 2: stri[0] == stri[1]
	if stri[0] == stri[-1]: return isPalindrome(stri[1:-1])
	return False
	
print(isPalindrome('awesome')) # False
print(isPalindrome('foobar')) # False
print(isPalindrome('tacocat')) # True