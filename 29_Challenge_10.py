# Rotation Check 
A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2, 3]

def is_rotation(A, B):
	if len(A) != len(B):
		return False
	key = A[0]
	key_index = -1
	for i in range(len(B)):
		if key == B[i]:
			key_index = i
			break

	if key_index == -1:
		return False

	for i in range(len(A)):
		j = (key_index+i) % len(A)
		if A[i] != B[j]:
			return False
	return True

print(is_rotation(A,B))