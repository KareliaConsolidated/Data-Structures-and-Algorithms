# Reverse the Words in Sentence
# Given a sentence, Given a sentence, reverse each word in the sentence while keeping the order the same!
def word_flipper(string):
	"""
	Flip the individual words in a sentence

	Args:
	our_string(string): Strings to have individual words flip
	Returns:
	string: String with words flipped
	"""	

	words = string.split(" ")
	# for char in range(len(words)):
	# 	words[char] = words[char][::-1]
	# return ' '.join(words)
	return ' '.join([char[::-1] for char in words])

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")