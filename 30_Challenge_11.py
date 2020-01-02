# Strings - Non Repeating Character
def non_repeating(stri):
	count = {}
	for i in range(len(stri)):
		char = stri[i]
		if char in count:
			count[char] += 1
		else:
			count[char] = 1
	for char in stri:
		if count[char] == 1:
			return char
	return None

print(non_repeating('aabcb')) # c
print(non_repeating('xxyz')) # y , return first one
print(non_repeating('aabb')) # None