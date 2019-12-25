# Multiple Pointers
# Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition
# Very efficient for solving problems with minimal space complexity as well.

# Write a function called sumZero which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist

############### METHOD 01 ###############

def sumzero(sort_arr):
	for i in sort_arr:
		if i == 0:
			continue
		if (-1 * i) in sort_arr:
			return [i, -i]

print(sumzero([-3, -2, -1, 0, 1, 2, 3])) # [-3, 3]
print(sumzero([-2, 0, 1, 3])) # None
print(sumzero([1, 2, 3])) # None

############### METHOD 02 ###############
# Time Complexity - O(n), Space Complexity - O(1)

def sumzero(sort_arr):
	left = 0
	right = len(sort_arr) - 1
	while left < right:
		sumarr = sort_arr[left] + sort_arr[right]
		if sumarr == 0:
			return [sort_arr[left],sort_arr[right]]
		elif sumarr > 0:
			right -= 1
		else:
			left += 1

print(sumzero([-4, -3, -2, -1, 0, 1, 2, 3, 10])) # [-3, 3]
print(sumzero([-3, -2, -1, 0, 1, 2, 3])) # [-3, 3]
print(sumzero([-2, 0, 1, 3])) # None
print(sumzero([1, 2, 3])) # None