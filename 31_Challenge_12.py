# Strings - One Away Strings
def is_one_away_same_length(s1,s2):
	count_diff = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			count_diff += 1
			if count_diff > 1:
				return False
	return True


# Assumption: s1 length == s2 length + 1
def is_one_away_diff_lengths(s1, s2):
	i = 0
	count_diff = 0
	while i < len(s2):
		if s1[i+count_diff] == s2[i]:
			i += 1
		else:
			count_diff += 1
			if count_diff > 1:
				return False
	return True

def is_one_away(s1,s2):
	if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
		return False
	elif len(s1) == len(s2):
		return is_one_away_same_length(s1,s2)
	elif len(s1) > len(s2):
		return is_one_away_diff_lengths(s1,s2)
	else:
		return is_one_away_diff_lengths(s2,s1)

print(is_one_away('abcde','abfde')) # True
print(is_one_away('abcde','abde')) # True
