# Write a function called charCount ?

########### METHOD ##############
# def charCount(stg):
# 	# In case if string is empty !
# 	if len(stg) == 0: return False
# 	# Creating an object to store character count and to return at the end
# 	chrDict = {}
# 	# Converting String to Lowercase to avoid discrepancies
# 	char = stg.lower()
# 	# Iterating over string
# 	for i in char:
# 		if i.isalnum():
# 			# if i in chrDict:
# 			# 	chrDict[i] += 1
# 			# else:
# 			# 	chrDict[i] = 1
# 			chrDict[i] = chrDict[i] + 1 if i in chrDict else 1
# 	return chrDict

import re
def charCount(stg):
	if stg is None: return False

	stg = stg.lower()

	regex = re.compile('[^A-Za-z0-9]')

	stg = regex.sub('', stg)

	return {char: stg.count(char) for char in set(stg)}

print(charCount("")) # False
print(charCount("hhh") ) # {'h': 3}
print(charCount("code in dna")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1}
print(charCount("CodeInDna")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1}
print(charCount("Code In Dna")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1}
print(charCount("CodeInDna007")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1, '0': 2, '7': 1}
print(charCount("Code In Dna 007")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1, '0': 2, '7': 1}
print(charCount("Code In Dna 007 !")) # {'c': 1, 'o': 1, 'd': 2, 'e': 1, 'i': 1, 'n': 2, 'a': 1, '0': 2, '7': 1}