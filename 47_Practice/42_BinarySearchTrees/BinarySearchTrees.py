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

	def find(self, target):
		if self.root is None: return False

		currentNode = self.root

		while currentNode is not None:
			if target == currentNode.val: 
				return True
			elif target > currentNode.val:
				currentNode = currentNode.right
			else:
				currentNode = currentNode.left
		return False

bst = BST()
bst.insert(10).insert(5).insert(2).insert(7).insert(13).insert(11).insert(16)
print(bst.root.val)
print(bst.root.left.val)
print(bst.root.left.left.val)
print(bst.root.left.right.val)
print(bst.root.right.val)
print(bst.root.right.left.val)
print(bst.root.right.right.val)
print(bst.find(12))