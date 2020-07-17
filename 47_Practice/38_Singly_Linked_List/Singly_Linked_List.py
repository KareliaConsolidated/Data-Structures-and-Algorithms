class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self, val):
		NewNode = Node(val)
		if self.head is None:
			self.head = NewNode
			self.tail = self.head
		else:
			self.tail.next = NewNode
			self.tail = NewNode
		self.length += 1
		return self

	def traverse(self):
		current = self.head
		while current is not None:
			print(current.val)
			current = current.next

	def pop(self):
		if self.length == 0: return None
		currNode = self.head
		prevNode = currNode
		while currNode.next is not None:
			prevNode = currNode
			currNode = currNode.next
		self.tail = prevNode
		prevNode.next = None
		self.length -= 1
		return currNode.val



SLL = SinglyLinkedList()
SLL.push('A')
#SLL.traverse()
print(SLL.pop())
#SLL.traverse()