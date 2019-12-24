# ===================================================================#
# Write a function which takes two numbers and returns their sum
# ===================================================================#
# 1. Can I restate the problem in my own words ?
# 2. What are the inputs that go into the problem ?
# 3. What are the outputs that should come from the solution to the problem ?
# 4. Can the outputs be determined from the inputs ? In other words, do I have enough information to solve the problem ?
# 5. How should I label the important pieces of data that are a part of the problem 

# ===============================================================================================#
# Write a function which takes in a string and returns count of each character in a string ?
# ===============================================================================================#
import re
def charCount(str):
	obj = {}
	for i in range(len(str)):
		char = str[i].lower()
		if re.search("[a-z0-9]", char):
			if char.lower() in obj:
				obj[char] += 1
			else:
				obj[char] = 1
		else:
			pass
	return obj

print(charCount('Consolidated1.12345345!@3'))
