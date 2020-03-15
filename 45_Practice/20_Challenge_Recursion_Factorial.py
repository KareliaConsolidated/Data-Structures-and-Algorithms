# Factorial
# Write a function which accepts a number and returns the factorial of that number. A factorial is the product of an integer and all the integers below itl e.g. factorial four is equal to 24. factorial zero is always 1.
def factorial(num):
	if num == 0 : return 1
	return num * factorial(num-1)

print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(4)) # 24
print(factorial(7)) # 5040