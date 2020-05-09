# Multiple Pointers - averagePair
# Write a function called averagePair. Given a sorted array of integers and a target average, determine if there is a pair of values in the array where the average of the pair equals the target average. There may be more than one pair that matches the average target.

# Constraints: Time :: O(N), Space :: O(1)

def averagePair(arr, val):
	start = 0
	end = len(arr)-1
	while start < end:
		avg = (arr[start]+arr[end])/2
		if avg == val:
			return True
		elif avg < val:
			start += 1
		else:
			end -= 1
	return False

print(averagePair([1,2,3],2.5)) # True
print(averagePair([1,3,3,5,6,7,10,12,19],8)) # True
print(averagePair([-1,0,3,4,5,6],4.1)) # False
print(averagePair([],4)) # False