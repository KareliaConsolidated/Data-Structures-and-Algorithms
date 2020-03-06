def charCount(string):
	collector = {}
	unknown = {}
	for char in string.lower():
		if isAlNum(char):
			if char in collector:
				collector[char] += 1
			else:
				collector[char]	= 1
		else:
			if char in unknown:
				unknown[char] += 1
			else:
				unknown[char]	= 1
	return collector, unknown			 

def isAlNum(char):
	convert = ord(char)
	if (convert > 47 and convert <58) or (convert > 64 and convert <91) or (convert > 96 and convert <123):
		return True
	return False	

print(charCount('KareliaConsolidated')) # True
print(charCount('Kare@@@liaCo$$$nsolidat#ed#')) # True
# ({'k': 1, 'a': 3, 'r': 1, 'e': 2, 'l': 2, 'i': 2, 'c': 1, 'o': 2, 'n': 1, 's': 1, 'd': 2, 't': 1}, {})
# ({'k': 1, 'a': 3, 'r': 1, 'e': 2, 'l': 2, 'i': 2, 'c': 1, 'o': 2, 'n': 1, 's': 1, 'd': 2, 't': 1}, {'@': 3, '$': 3, '#': 2})