# Like merge sort, exploits the fact that arrays of 0 or 1 element are always sorted.
# Works by selecting one element (called the "pivot") and finding the index where the pivot should end up in the sorted array.
# Once the pivot is positioned appropriately, quick sort can be applied on either side of the pivot.

# Pivot Helper
# In order to implement merge sort, its useful to first implement a function responsible arranging elements in an  array on either side of a pivot.
# Given an array, this helper function should designate an element as the pivot.
# It should then rearrange elements in the array so that all values less than the pivot are moved to the left of the pivot and all values greater than the pivot are moved to the right of the pivot.
# The order of elements on either side of the pivot doesn't matter!
# The helper should do this in place, that is, it should not create a new array.
# When complete, the helper should return the index of the pivot.

# Picking a Pivot
# The runtime of quick sort depends in part on how one selects the pivot.
# Ideally, the pivot should be chosen so that it's roughly the median value in the data set you're sorting.
# For simplicity, we'll always choose the pivot to be the first element

# Pivot Pseudocode
# It will help to accept three arguments: an array, a start index, and an end index (these can default to 0 and the array length minus 1, respectively)
# Grab the pivot from the start of the array
# Store the current pivot index in a variable (this will keep track of where the pivot should end up)
# Loop through the array from the start until the end
	# If the pivot is greater than the current element, increment the pivot index variable and then the current element with the element at the pivot index.
# Swap the starting element(i.e. the pivot) with the pivot index.
# Return the pivot index.

# QuickSort Pseudocode
# Call the Pivot Helper on the Array
# When the helper returns to you the updated pivot index, recursively call the pivot helper on the subarray to the left of that index, and the subarray to the right of that index.
# Your base case occurs when you consider a subarray with less than 2 elements.

def quickSort(arr):
	elements = len(arr)

	# Base Case:
	if elements < 2:
		return arr

	current_position = 0 # Position of the Pivot Element

	for i in range(1,elements):
		if arr[i] <= arr[0]:
			arr[i], arr[current_position] = arr[current_position], arr[i]
	arr[0], arr[current_position] = arr[current_position], arr[0] # Bring Pivot to Its Appropriate Position

	# Sort the Elements to the Left of the Pivot
	left = quickSort(arr[0:current_position])
	# Sort the Elements to the Right of the Pivot
	right = quickSort(arr[current_position+1:elements])
	# Merging Everything Together
	arr = left + [arr[current_position]] + right

	return arr

print(quickSort([4,6,9,1,2,5,3]))
arr1  = [4,6,9,1,2,5,3]
print(arr1[0:4])