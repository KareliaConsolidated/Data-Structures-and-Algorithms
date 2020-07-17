# Radix Sort
def getDigit(num, i):
	return abs(num) // pow(10, i) % 10

# def digitCount(num):
# 	return len(str(abs(num)))

import math
def digitCount(num):
	if num == 0: return 1
	return math.floor(math.log10(abs(num))) + 1

def mostDigits(arr):
	if len(arr) == 0: return 0
	return digitCount(max(arr))

# def mostDigits(nums):
# 	maxDigits = 0 
# 	for i in range(len(nums)):
# 		maxDigits = max(maxDigits, digitCount(nums[i]))
# 	return maxDigits


def radixSort(nums):
	maxDigitCount = mostDigits(nums)
	for k in range(maxDigitCount):
		digitBuckets = [[] for _ in range(10)]
		for i in range(len(nums)):
			digit = getDigit(nums[i], k)
			digitBuckets[digit].append(nums[i])
		nums = [item for sublist in digitBuckets for item in sublist]
	return nums

print(radixSort([23,345,5467,12,2345,9852,147])) # [12, 23, 147, 345, 2345, 5467, 9852]

print(radixSort([123,3245,546337,122,2345,9852,147])) # [122, 123, 147, 2345, 3245, 9852, 546337]