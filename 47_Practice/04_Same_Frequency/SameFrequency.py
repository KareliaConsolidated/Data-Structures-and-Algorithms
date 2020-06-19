# Frequency Counter - sameFrequency
# Write a function called sameFrequency. Given two positive integers, find out if the two numbers have the same frequency of digits. 
# Time Complexity Should be O(N)

############### METHOD 01 ###############

from collections import Counter
def sameFrequency(num1, num2):
	return Counter(str(num1)) == Counter(str(num2))

############### METHOD 02 ###############

def sameFrequency(num1, num2):
	if len(str(num1)) != len(str(num2)):
		return False

	numDict_01 = {i:str(num1).count(i) for i in str(num1)}
	numDict_02 = {i:str(num2).count(i) for i in str(num2)}

	for key, val in numDict_01.items():
		if key not in numDict_02.keys():
			return False
		elif numDict_01[key] != numDict_02[key]:
			return False
	return True