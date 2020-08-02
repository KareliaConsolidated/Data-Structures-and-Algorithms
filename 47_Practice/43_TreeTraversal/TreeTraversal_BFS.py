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

	def BFS(self):
		node = self.root
		queue = []
		outdata = []
		queue.append(node)
		while len(queue) != 0:
			node = queue.pop(0)
			outdata.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		return outdata

	def DFS_PRE(self):
		outdata = []
		current = self.root
		def DFS_helper(outdata, current):
			outdata.append(current.val)
			if current.left:
				DFS_helper(outdata, current.left)
			if current.right:
				DFS_helper(outdata, current.right)
		DFS_helper(outdata, current)
		return outdata

	def DFS_POST(self):
		outdata = []
		current = self.root
		def DFS_helper(outdata, current):
			if current.left:
				DFS_helper(outdata, current.left)
			if current.right:
				DFS_helper(outdata, current.right)
			outdata.append(current.val)
		DFS_helper(outdata, current)
		return outdata

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

bst = BST()
bst.insert(10).insert(5).insert(2).insert(7).insert(13).insert(11).insert(16)
print(bst.BFS()) # [10, 5, 13, 2, 7, 11, 16]
print(bst.DFS_PRE()) # [10, 5, 2, 7, 13, 11, 16]
print(bst.DFS_POST()) # [2, 7, 5, 11, 16, 13, 10]
print(bst.DFS_IN()) # [2, 5, 7, 10, 11, 13, 16]