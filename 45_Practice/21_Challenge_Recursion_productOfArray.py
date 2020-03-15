# Write a function called ProductofArray which takes in an array of numbers and returns the product of them all.
def ProductofArray(arr):
	if len(arr) == 0: return 1
	return arr[0] * ProductofArray(arr[1:])

print(ProductofArray([1,2,3])) # 6
print(ProductofArray([1,2,3,10])) # 60