# Applications (Its a LIFO Data Structure):
# CallStack Functions (Recursive) | Undo/Redo | Browsing History
# Big O of Stacks - Insertion - O(1) | Removal - O(1) | Searching - O(N) | Access - O(N)

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Stack:
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def push(self, val):
		newNode = Node(val)
		if self.first == None:
			self.first = newNode
			self.last = newNode
		else:
			newNode.next = self.first
			self.first = newNode
		self.size += 1
		return self

	def pop(self):
		if self.size == 0: 
			return None
		else:
			currentNode = self.first
			nextNode = currentNode.next
			currentNode.next = None
			self.first = nextNode
			self.size -= 1
		return currentNode.val

	def traverse(self):
		currentNode = self.first
		while currentNode is not None:
			print(currentNode.val)
			currentNode = currentNode.next

stack = Stack()
stack.push(1).push(2).push(3)
stack.traverse()
print(stack.pop())

Stack_Array = []
Stack_Array.append(1)
Stack_Array.append(2)
Stack_Array.append(3)
Stack_Array.append(4)
print(Stack_Array)
print(f"Popped Out Last Node : {Stack_Array.pop()}")