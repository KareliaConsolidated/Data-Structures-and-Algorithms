# Merging Arrays Pseudocode
# Create an Empty Array, Take a Look at the Smallest Values in Each Input Array.
# While there are still values we haven't looked at..
	# If the value in the first array is smaller than the value in the second array, push the value in the first array into our results and move on the next value in the first array.
	# If the value in the first array is larger than the value in the second array, push the value in the second array into our results and move on the next value in the second array.
	# Once exhausted one array, push in all remaining values from the other array.

def merge(arr1, arr2):
	
	results = []
	i = j = 0

	while (i<len(arr1)) and (j<len(arr2)):
		if arr2[j] > arr1[i]:
			results.append(arr1[i])
			i+= 1
		else:
			results.append(arr2[j])
			j+= 1

	while i < len(arr1):
		results.append(arr1[i])
		i += 1

	while j < len(arr2):
		results.append(arr2[j])
		j += 1

	return results

# print(merge([1,10,50],[2,14,99,100]))

# Merge Sort Pseudocode

# Break up the array into halves until you have arrays that are empty or have one element.
# Once you have smaller sorted arrays, merge those arrays with other sorted arrays until you are back at the full length of the array
# Once the array has been merged back together, return the merged (and sorted !) array.
def mergeSort(arr):
	if len(arr) <= 1: return arr
	mid = len(arr) // 2
	left = mergeSort(arr[:mid])
	right = mergeSort(arr[mid:])
	return merge(left, right)

print(mergeSort([10,34,23,36,76,73,1,9,2]))	