class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class DLL:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self, val):
		newNode = Node(val)
		if self.head is None:
			self.head = newNode; self.tail = newNode
		else:
			newNode.prev = self.tail
			self.tail.next = newNode
			self.tail = newNode
		self.length += 1
		return self

	def traverse(self):
		currentNode = self.head
		while currentNode is not None:
			print(currentNode.val)
			currentNode = currentNode.next

	def pop(self):
		if self.length == 0: return None
		
		currentNode = self.tail

		if self.length == 1: 
			self.head = None; self.tail=None
		else:
			self.tail = currentNode.prev
			self.tail.next = None
			currentNode.prev = None
		
		self.length -= 1

		return currentNode

	def shift(self):
		if self.length == 0: return None
		
		currentFirst = self.head

		if self.length == 1:
			self.head = None; self.tail = None
		else:
			self.head = currentFirst.next
			currentFirst.next = None
			self.head.prev = None
		self.length -= 1
		return currentFirst

	def unshift(self, val):
		newNode = Node(val)
		if self.head is None:
			self.head = newNode; self.tail = newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode
		self.length += 1
		return self

	def get(self, idx):
		if idx < 0 or idx >= self.length: return None
		dividelength  = (self.length - 1)// 2
		if idx <= dividelength:
			currentNode = self.head
			counter = 0
			while counter != idx:
				currentNode = currentNode.next
				counter += 1
		else:
			currentNode = self.tail
			counter = self.length - 1
			while counter != idx:
				currentNode = currentNode.prev
				counter -= 1
		return currentNode
	
	def set(self, idx, val):
		NodeFound = self.get(idx)
		if NodeFound:
			NodeFound.val = val
			return True
		return False

	def insert(self, idx, val):
		if idx < 0 or idx > self.length: return False
		if idx == 0: return self.unshift(val)
		if idx == self.length: return self.push(val)

		newNode = Node(val)
		prevNode = get(idx-1)
		
		currNode = prevNode.next
		prevNode.next = newNode
		newNode.next = currNode
		newNode.prev = prevNode
		currNode.prev = newNode

		self.length += 1

		return True

	def remove(self, idx):
	    if idx < 0 and idx >= self.length:
	        return None
	    if idx == self.length - 1:
	        return self.pop()
	    if idx == 0:
	        return self.shift()

	    removedNode = self.get(idx)
	    prevNode = removedNode.prev
	    nextNode = removedNode.next
	    prevNode.next, nextNode.prev = nextNode, prevNode
	    removedNode.prev, removedNode.next = None, None

	    self.length -= 1

	    return removedNode


	def reverse(self):
		currentNode = self.head
		self.head, self.tail = self.tail, self.head
		prevNode = None
		while currentNode is not None:
			nextNode = currentNode.next
			currentNode.next = prevNode
			prevNode = currentNode
			currentNode = nextNode
		return self


dll = DLL()		
dll.push(1).push(2).push(3).push(4)
# print(dll.pop())
# # dll.traverse()
# dll.shift()
# dll.shift()
# dll.traverse()
print(dll.get(1))
print(dll.set(1,29))
dll.insert(4, 45)
dll.traverse()
dll.reverse()
dll.traverse()