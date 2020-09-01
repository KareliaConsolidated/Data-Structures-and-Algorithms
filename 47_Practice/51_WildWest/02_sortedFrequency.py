# Given a sorted array and a number, write a function called sortedFrequency that counts the occurences of the number in the array

############### METHOD 01 ####################

from collections import Counter	
def sortedFrequency(arr, num):
	return Counter(arr)[num]

# ############### METHOD 02 ####################

def sortedFrequency(arr, num):
	count = 0
	for i in range(len(arr)):
		if arr[i] == num:
			count += 1
	return count

############### METHOD 03 ####################

def OccurenceSearch(arr, num, SearchFirst):
	left = 0
	right = len(arr) - 1

	result = -1

	while left <= right:
		mid = (left + right) // 2

		if num == arr[mid]:
			result = mid
			if SearchFirst:
				right = mid - 1
			else:
				left = mid + 1
		elif num < arr[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return result

def sortedFrequency(arr, num):
	FirstOccIdx = OccurenceSearch(arr, num, True)
	LastOccIdx = OccurenceSearch(arr, num, False)
	Length = LastOccIdx - FirstOccIdx + 1
	return Length

print(sortedFrequency([1,2,2,2,2,3,3,4],2)) # 4
print(sortedFrequency([1,1,2,2,2,2,3], 2)) # 4
print(sortedFrequency([1,1,2,2,2,2,3], 3)) # 1
print(sortedFrequency([1,1,2,2,2,2,3], 1)) # 2
print(sortedFrequency([1,1,2,2,2,2,3], 4)) # -1