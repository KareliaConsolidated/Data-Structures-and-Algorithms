# Count Unique Values
# Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.

############### METHOD 01 ###############

# def countUniqueValues(sort_arr):
# 	return len(set(sort_arr))

############### METHOD 02 ###############

def countUniqueValues(sort_arr):
	if len(sort_arr) == 0: return 0
	i = 0
	for j in range(1,len(sort_arr)):
		if sort_arr[i] != sort_arr[j]:
			i += 1
			sort_arr[i] = sort_arr[j]
	return i + 1

print(countUniqueValues([1,1,1,1,1,2])) # 2
print(countUniqueValues([1,1,1,1,1,2,3,3,4,4,12,12])) # 5
print(countUniqueValues([])) #  0
print(countUniqueValues([-2,-1,-1,0,1])) #  4