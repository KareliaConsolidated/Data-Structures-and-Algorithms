def linearSearch(arr,num):
	for i in range(len(arr)):
		if arr[i] == num:
			return i
	return -1

print(linearSearch([1,2,3,4,5],6)) # -1
print(linearSearch([1,2,3,4,5],3)) #  2

# O(1) - Best Case
# O(n) - Average Case
# O(n) - Worst Case