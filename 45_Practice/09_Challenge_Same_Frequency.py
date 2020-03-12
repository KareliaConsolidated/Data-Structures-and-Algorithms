# Frequency Counter - sameFrequency
# Write a function called sameFrequency. Given two positive integers, find out if the two numbers have the same frequency of digits. 
# Time Complexity Should be O(N)

from collections import Counter
def sameFrequency(num1, num2):
	return Counter(str(num1)) == Counter(str(num2))

def sameFrequency(num1, num2):
	if len(str(num1)) != len(str(num2)): return False

	numCount1 = {num1:str(num1).count(num) for num in str(num1)}
	numCount2 = {num2:str(num2).count(num) for num in str(num2)}

	for key, val in numCount1.items():
		if key not in numCount2.keys():
			return False
		elif numCount1[key] != numCount2[key]:
			return False
	return True

print(sameFrequency(182, 281)) # True
print(sameFrequency(34, 14)) # False
print(sameFrequency(3589578, 5879385)) # True
print(sameFrequency(22, 222)) # False