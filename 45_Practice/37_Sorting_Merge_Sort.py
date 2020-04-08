# Merging Arrays Pseudocode
# Create an Empty Array, Take a Look at the Smallest Values in Each Input Array.
# While there are still values we haven't looked at..
	# If the value in the first array is smaller than the value in the second array, push the value in the first array into our results and move on the next value in the first array.
	# If the value in the first array is larger than the value in the second array, push the value in the second array into our results and move on the next value in the second array.
	# Once exhausted one array, push in all remaining values from the other array.

def merge(arr1, arr2):
	
	results = []
	i, j = 0, 0

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

print(merge([1,10,50],[2,14,99,100]))