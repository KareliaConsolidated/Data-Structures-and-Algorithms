# Find Closest Value in BST
# You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. You are also given a target integer value; write a function that finds the closest value to that target value contained in the BST. Assume that there will only be one closest value.
# Sample Input:
#         10    ,12
#        /  \
#       5    15
#      / \   / \
#     2   5 13 22
#    /        \
#   1         14
# Sample Output: 13

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def insert(self, val):
		newNode = Node(val)

		if self.root is None:
			self.root = newNode
			return self

		currentNode = self.root

		while True:
			if newNode.val > currentNode.val:
				if currentNode.right:
					currentNode = currentNode.right
				else:
					currentNode.right = newNode
					return self
			else:
				if currentNode.left:
					currentNode = currentNode.left
				else:
					currentNode.left = newNode
					return self

	def DFS_IN(self):
		outdata = []
		current = self.root
		def DFS_helper(outdata, current):
			if current.left:
				DFS_helper(outdata, current.left)
			outdata.append(current.val)				
			if current.right:
				DFS_helper(outdata, current.right)
		DFS_helper(outdata, current)
		return outdata

	def closest_node(self, target):
		if self.root is None:
			return None

		currNode = self.root
		min_diff = float('inf')

		while currNode is not None:
			if min_diff > abs(target - currNode.val):
				closest = currNode.val

			if target > currNode.val:
				currNode = currNode.right
			elif target < currNode.val:
				currNode = currNode.left
			else:
				break

		return closest

bst = BST()
bst.insert(10).insert(5).insert(15).insert(2).insert(5).insert(13).insert(22).insert(1).insert(14)
print(bst.DFS_IN())
print(bst.closest_node(12))
