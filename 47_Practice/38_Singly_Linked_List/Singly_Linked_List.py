class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class SLL:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self, val):
		newNode = Node(val)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode
		self.length += 1
		return self

	def traverse(self):
		if self.head is None: return None
		currentNode = self.head
		while currentNode is not None:
			print(currentNode.val)
			currentNode = currentNode.next

	def pop(self):
		if self.length == 0: return None

		currentNode = self.head
		prevNode = currentNode

		while currentNode.next is not None:
			prevNode = currentNode
			currentNode = currentNode.next

		prevNode.next = None
		self.tail = prevNode

		if self.length == 1: self.head = None; self.tail = None

		self.length -= 1

		return currentNode

	def shift(self):
		if not self.head: return None 

		currNode = self.head
		self.head = currNode.next

		self.length -= 1
		if self.length == 0: self.tail = None

		return currNode.val

	def unshift(self, val):
		newNode = Node(val)

		if self.length == 0: self.head = newNode; self.tail= newNode

		if self.length >= 1:
			newNode.next = self.head
			self.head = newNode

		
		self.length += 1
		
		return self



newNode = SLL()
newNode.push(1).push(2).push(3).push(4)
newNode.traverse()
newNode.pop()
newNode.pop()
newNode.traverse()
newNode.shift()
newNode.traverse()
newNode.shift()
newNode.traverse()
newNode.shift()
newNode.unshift(56).unshift(67)
newNode.traverse()