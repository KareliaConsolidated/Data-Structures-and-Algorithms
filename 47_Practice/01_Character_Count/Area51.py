# Write a function called charCount

def charCount(stg):
	if len(stg) == 0: return False
	charCount = {}
	for char in stg:
		if char.isalnum():
			if char not in charCount:
				charCount[char] = 1
			else:
				charCount[char] += 1
	return charCount

print(charCount("")) # False
print(charCount("hhh") ) # {'h': 3}
print(charCount("code in dna")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1}
print(charCount("CodeInDna")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1}
print(charCount("Code In Dna")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1}
print(charCount("CodeInDna007")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1, '0': 2, '7': 1}
print(charCount("Code In Dna 007")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1, '0': 2, '7': 1}
print(charCount("Code In Dna 007 !")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1, '0': 2, '7': 1}
	