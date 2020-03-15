# Power
# Write a function called power which accepts a base and an exponent. The function should return the power of the base to the exponent. This function should mimic the functionality of Math.pow()
def power(num,exp):
	if exp == 0: return 1
	return num * power(num, exp-1)

print(power(4,5)) # 1024