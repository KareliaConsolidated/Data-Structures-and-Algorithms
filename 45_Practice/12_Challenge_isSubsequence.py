# Multiple Pointers - isSubsequence
# Write a function called isSubsequence which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string without their order changing.
def isSubsequence(substr, fullstr):
	start = 0
	end = 0
	while end < len(fullstr):
		if substr[start] == fullstr[end]:
			start += 1
		if start == len(substr):
			return True
		end += 1
	return False

print(isSubsequence('hello', 'hello world')) # True
print(isSubsequence('sing', 'sting')) # True
print(isSubsequence('abc','abracadabra')) # True
print(isSubsequence('abc','acb')) # False