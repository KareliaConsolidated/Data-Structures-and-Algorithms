# Multiple Pointers - averagePair
# Write a function called averagePair. Given a sorted array of integers and a target average, determine if there is a pair of values in the array where the average of the pair equals the target average. There may be more than one pair that matches the average target.

# Constraints: Time :: O(N), Space :: O(1)

def averagePair(arr, avg):
	if len(arr) == 0: return False
	start = 0
	end = len(arr) - 1

	while start < end:
		Calaverage = (arr[start] + arr[end]) / 2
		if Calaverage < avg:
			start += 1
		elif Calaverage > avg:
			end -= 1
		else:
			return True
	return False