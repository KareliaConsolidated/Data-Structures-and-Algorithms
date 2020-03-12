# Anagrams
# Given two strings, write a function to determine if the second string is an anagram of the first. Ana anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema formed from iceman.

############### METHOD 01 ###############
from collections import Counter
def validAnagram(str1,str2):
	return Counter(str1) == Counter(str2)

############### METHOD 02 ###############
def valid Anagram(str1, str2):
	anagram_dict = {}
	if len(str1) != len(str2):
		return False

	DictStr1 = {letter:str1.count(letter) for letter in str1}
	DictStr2 = {letter:str2.count(letter) for letter in str2}

	for key, val in DictStr1.items():
		if not key in DictStr2.keys():
			return False
		elif DictStr1[key] != DictStr2[key]:
			return False
	return True

print(validAnagram('','')) # True
print(validAnagram('anagram','nagaram')) # True
print(validAnagram('rat', 'car')) # False
print(validAnagram('Qwerty', 'tyerwQ')) # True