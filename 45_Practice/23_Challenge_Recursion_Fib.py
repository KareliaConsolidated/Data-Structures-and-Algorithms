# Fib
# Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence. 
# Recall that the Fibonacci sequence is the sequence of whole numbers 1,1,2,3,5,8.. which starts with 1 and 1, 
# where every number thereafter is equal to the sum of the previous two numbers.

def fib(num):
	if num == 1: return 0
	if num == 2: return 1
	return fib(num - 1) + fib(num-2)

print(fib(4)) # 3
print(fib(10)) # 55 
print(fib(28)) # 317811
print(fib(35)) # 9227465