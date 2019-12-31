# Most Frequent
arr = [1,3,1,3,2,1]
def most_frequent(arr):
	max_count = -1
	max_item = None
	count = {}
	for i in range(len(arr)):
		val = arr[i]
		if val in count:
			count[val] += 1
		else:
			count[val] = 1
		if count[val] > max_count:
			max_count = count[val]
			max_item = val
		return max_item

print(most_frequent(arr)) # 1