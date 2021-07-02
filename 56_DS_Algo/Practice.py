def char_count(string):
	if not string: return False

	charCount = {}

	for char in string.lower():
		if char.isalnum():
			charCount[char] = charCount.get(char, 0) + 1

	return charCount

print(f"Value Count : {char_count('Anubhav@90')}")