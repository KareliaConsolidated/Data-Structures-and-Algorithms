# Common Elements between two Arrays
A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]

def common_elements(arr1,arr2):
	point1 = 0
	point2 = 0
	common_elem = []
	while point1 < len(arr1) and point2 < len(arr2):
		if arr1[point1] == arr2[point2]:
			common_elem.append(arr1[point1])
			point1 += 1
			point2 += 1
		elif arr1[point1] > arr2[point2]:
			point2 += 1
		else:
			point1 += 1
	return common_elem

print(common_elements(A,B))