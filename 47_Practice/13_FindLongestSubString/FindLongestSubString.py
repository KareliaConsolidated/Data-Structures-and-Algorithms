# Sliding Window - findLongestSubstring
# Write a function called findLongestSubstring, which accepts a string and returns the length of the longest substring with all distinct characters.

def FindLongestSubString(string):
	start = 0
	maxLen = 0
	seen = {}
	for end in range(len(string)):
		if string[end] in seen:
			start = max(start, seen[string[end]] + 1)
		maxLen = max(maxLen, end - start + 1)
		seen[string[end]] = end
	return maxLen