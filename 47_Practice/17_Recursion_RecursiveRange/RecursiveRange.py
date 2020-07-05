# Write a function called Recursive Range which accepts a number and adds up all the numbers from 0 to the number passed to the function.

def recursiveRange(num):
	if num == 1: return 1
	return num + recursiveRange(num-1)

