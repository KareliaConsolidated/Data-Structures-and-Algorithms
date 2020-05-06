# Frequency Counter / Multiple Pointers - areThereDuplicates
# Implement a function called, areThereDuplicates which accepts a variable number of arguments, and checks whether there are any duplicates among the arguments passed in.
# You can solve this using the frequency counter pattern OR the multiple pointers pattern.
# Time - O(N) # Space - O(N)

############## METHOD 01 - Multiple Pointers ##############

def areThereDuplicates(*args):
	args = sorted(list(args))
	startpt=0
	nextpt=1
	while nextpt < len(args):
		if args[startpt] == args[nextpt]:
			return True
		startpt += 1
		nextpt += 1
	return False

############## METHOD 02 - Frequency Counter ##############

def areThereDuplicates(*args):
	collections = {num:list(args).count(num) for num in list(args)}
	for key in collections:
		if collections[key] > 1:
			return True
	return False

############## METHOD 03 - One Liner ##############

def areThereDuplicates(*args):
	return len(set(args)) != len(list(args))

############## METHOD 04 - Frequency Counter ##############

def areThereDuplicates(*args):
	args = list(args)
	for num in args:
		counter = args.count(num)
		if counter > 1:
			return True
	return False

print(areThereDuplicates(1, 2, 3)) # False
print(areThereDuplicates(2, 2, 1)) # True
print(areThereDuplicates('a', 'b', 'c', 'c')) # True