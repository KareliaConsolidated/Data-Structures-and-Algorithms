def NaiveSearch(LongStr, PattenStr):
	
	count = 0
	
	for i in range(len(LongStr)):
		j = 0
		while j < len(PattenStr):
			if PattenStr[j] != LongStr[i+j]:
				break
			if j == len(PattenStr)-1:
				count += 1
			j+=1
	return count

print(NaiveSearch("lorie loled", "lol")) # 1
print(NaiveSearch("wowomgzomg", "omg")) # 2