### Radix Sort ###
# Radix Sort is a special sorting algorithm that works on lists of numbers.
# It never makes comparisions between elements!
# It exploits the fact that information about the size of a number is encoded in the number of digits.
# More digits means a bigger number!
 
# Radix Sort Helpers
# In order to implment radix sort, its helpful to build a few helper function first:
# getDigit(num,place)- returns the digit in num at the given place value 
# getDigit(12345, 0) - 5
# getDigit(12345, 1) - 4
# getDigit(12345, 2) - 3

def getDigit(num, i):
	return abs(num) // pow(10,i) % 10

# print(getDigit(12345,2)) #  3

# digitCount(num) - returns the number of digits in num
# digitCount(1) - 1
# digitCount(13) - 2

import math
def digitCount(num):
	if num == 0: return 1
	return math.floor(math.log10(abs(num))) + 1

# print(digitCount(137)) # 3

# mostDigits(nums) - Given an array of numbers, returns the number of digits in the largest numbers in the list
# mostDigits([1234, 56, 7]) - 4
# mostDigits([123456, 56, 7]) - 6
def mostDigits(nums):
	maxDigits = 0 
	for i in range(len(nums)):
		maxDigits = max(maxDigits, digitCount(nums[i]))
	return maxDigits

# print(mostDigits([123456, 56, 7])) # 6

# Radix Sort Pseudocode
# Define a function that accepts list of numbers
# Figure out how many digits the largest number has
# Loop from k=0 up to this largest number of digits
# For each iteration of the loop:
	# Create buckets for each digit (0 to 9)
	# Place each number in the corresponding bucket based on its kth digit
# Replace our existing array with values in our buckets, starting with 0 and going up to 9
# Return list at the end.

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