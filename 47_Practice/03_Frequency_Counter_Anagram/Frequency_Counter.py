# Anagrams
# Given two strings, write a function to determine if the second string is an anagram of the first. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
############### METHOD 01 ###############
def validAnagrams(str1, str2):
	if len(str1) != len(str2):
		return False

	charCount1 = {letter:str1.count(letter) for letter in str1}
	charCount2 = {letter:str2.count(letter) for letter in str2}

	for key, val in charCount1.items():
		if key not in charCount2.keys():
			return False
		elif charCount1[key] != charCount2[key]:
			return False
	return True

############### METHOD 02 ###############
from collections import Counter
def validAnagrams(str1, str2):
	if len(str1) != len(str2):
		return False
	return Counter(str1) == Counter(str2)