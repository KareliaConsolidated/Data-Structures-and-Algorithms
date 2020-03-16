# Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

################## METHOD # 01 ################## 

def flatten(arr):
	if len(arr) == 0: return arr
	if isinstance(arr[0], list):
		return flatten(arr[0]) + flatten(arr[1:])
	return arr[:1] + flatten(arr[1:])

print(flatten([1,2,3,[4,5]])) # [1,2,3,4,5]
print(flatten([[1,2],3,[4,5]])) # [1,2,3,4,5]

################## METHOD # 02 ################## 

def flattenArray(my_nest):
    # my_nest is a list, possibly nested, to ONE level
    my_flat = [] # initially empty, result list
    for my_item in my_nest:
        if type(my_item) is list:
            # if we have a list, then extend the result
            # with the item, an assumed flat list
            my_flat.extend(my_item)
        else: # otherwise append to the result, one item
            my_flat.append(my_item)
    return my_flat # now flattened list

print(flattenArray([1,2,3,[4,5]])) # [1,2,3,4,5]
print(flattenArray([[1,2],3,[4,5]])) # [1,2,3,4,5]    