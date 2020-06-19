# Frequency Counter / Multiple Pointers - areThereDuplicates
# Implement a function called, areThereDuplicates which accepts a variable number of arguments, and checks whether there are any duplicates among the arguments passed in.
# You can solve this using the frequency counter pattern OR the multiple pointers pattern.
# Time - O(N) # Space - O(N)

############## METHOD 01 ##############

def arethereduplicates(*args):
	collections = {val:list(args).count(val) for val in list(args)}
	for key in collections:
		if collections[key] > 1:
			return True
	return False

############## METHOD 02 ##############	

def arethereduplicates(*args):
	return len(set(args)) != len(list(args))


############## METHOD 03 ##############		

def arethereduplicates(*args):
	args = list(args)
	for num in args:
		counter = args.count(num)
		if counter > 1:
			return True
	return False