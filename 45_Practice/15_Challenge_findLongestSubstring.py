# Sliding Window - findLongestSubstring
# Write a function called findLongestSubstring, which accepts a string and returns the length of the longest substring with all distinct characters.

def findLongestSubstring(stri):
	longest = 0
	seen = {}
	start = 0

	for i in range(len(stri)):
		char = stri[i]
		if char in seen:
			start = max(start, seen[char])

		longest = max(longest, i-start+1)
		seen[char] = i+1
	return longest 

	
print(findLongestSubstring('')) # 0
print(findLongestSubstring('thisisawesome')) # 6
print(findLongestSubstring('thecatinthehat')) # 7
print(findLongestSubstring('bbbbb')) # 1
print(findLongestSubstring('longestsubstring')) # 8
print(findLongestSubstring('thisishowwedoit')) # 6