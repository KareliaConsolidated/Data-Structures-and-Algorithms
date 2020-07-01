# Multiple Pointers - isSubsequence
# Write a function called isSubsequence which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string without their order changing.

def isSubsequence(subStr, fullStr):
	subPtr = 0
	fullPtr = 0
	while fullPtr < len(fullStr):
		if subStr[subPtr] == fullStr[fullPtr]:
			subPtr += 1
		if subPtr == len(subStr):
			return True
		fullPtr += 1
	return False