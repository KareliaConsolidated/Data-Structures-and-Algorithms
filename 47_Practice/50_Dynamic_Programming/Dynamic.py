# ---------------------- PROBLEM 19 (RANDOM) ----------------------------------#
# Write a function called fib which accepts a number and returns the nth number
# in the Fibonacci sequence. Recall that the Fibonacci sequence of whole numbers
# 1,1,2,3,5,8...which starts with 1 and 1, and where every number therafter is 
# equal to the sum of the precious two numbers.

# Sample input: 10
# Sample output: 55

def fib_memo(number, memo = {2:1, 1:1}):
	if number in memo.keys():
		return memo[number]

	result = fib_memo(number-1) + fib_memo(number-2)

	memo[number] = result

	return result

def fib_table(number):
	if number<=2: return fibNums[number]
	fibNums = [0, 1, 1]
	for i in range(3, number+1):
		fibNums.append(fibNums[i-1] + fibNums[i-2])
	return fibNums[number]

def fib_chuja(number):
	a = 1
	b = 1
	for i in range(number-2):
		z = a+b
		a,b = b, z
	return z