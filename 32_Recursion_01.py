# Base Case: The Condition when the recursion ends.
def countDown(num):
	if num <= 0:
		print('All Done!')
		return 
	print(num)
	num -= 1
	countDown(num)

countDown(5) # 5 4 3 2 1 All Done!

def sumRange(num):
	if num == 1: return 1
	return num + sumRange(num-1)

print(sumRange(5)) # 15

def factorial(num):
	if num == 1: return 1
	return num * factorial(num-1)

print(factorial(5)) # 120