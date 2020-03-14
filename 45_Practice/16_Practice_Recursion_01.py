def countDown(num):
	if num <= 0:
		print('All Done!')
		return
	print(num)
	num -= 1
	countDown(num)

print(f"Output of countDown Function: {countDown(10)}")
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# All Done!

##########################################################

def sumRange(n):
	if n == 1: return 1
	return n + sumRange(n-1)

print(f"Output of sumRange Function: {sumRange(5)}") # 1

##########################################################

def factorial(n):
	if n == 1: return 1
	return n * factorial(n - 1)

print(f"Output of Factorial Function: {factorial(5)}") # 120	