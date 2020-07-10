def NaiveSearch(Full,Sub):

	count = 0

	for i in range(len(Full)):
		j = 0
		while j < len(Sub):
			if Sub[j] != Full[i+j]:
				break
			if j == len(Sub) - 1:
				count += 1
			j += 1
	return count

print(NaiveSearch("lorie loled", "lol")) # 1
print(NaiveSearch("wowomgzomg", "omg")) # 2