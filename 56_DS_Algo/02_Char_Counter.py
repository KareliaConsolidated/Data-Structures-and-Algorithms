
# ---------------------------------- PROBLEM 01 (RANDOM) ----------------------------------------------#
# Write a function that takes in a string and return count of each charcter in 
# the string. Assume allowed characters can only be alphabets and numbers.

# Sample input: 'aaaa'
# Sample output: {a: 4}

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def char_count(string):
	# if string is empty return False
	if not string: return False

	# Define an object to return in the end
	charCount = {}

	# Iterate over the lowercase characters
	for char in string.lower():
		# Check if char is alphanumeric
		if char.isalnum():
			# if char not in object, initialize it with 1, else add 1
			charCount[char] = charCount[char] + 1 if char in charCount else 1

	# Return object with char count
	return charCount

print(f"{char_count('Anubhav@90')}")

# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#

import re
def check_alnum(char):
	return bool(re.match('^[a-zA-Z0-9]+$', char))

def char_count_reg(string):
	if not string: return False

	charCount = {}

	for key in string.lower():
		if check_alnum(key):
			char_count[key] = charCount.get(key, 0) + 1

	return charCount

print(f"{char_count('Yashika@92')}")	