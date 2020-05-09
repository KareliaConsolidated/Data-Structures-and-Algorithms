def isSubsequence(substr, fullstr):
	ptrsub = 0
	ptrfull = 0
	while ptrfull < len(fullstr):
		if substr[ptrsub] == fullstr[ptrfull]:
			ptrsub += 1
		if ptrsub == len(substr):
			return True
		ptrfull += 1
	return False

print(isSubsequence('hello', 'hello world')) # True
print(isSubsequence('sing', 'sting')) # True
print(isSubsequence('abc','abracadabra')) # True
print(isSubsequence('abc','acb')) # False