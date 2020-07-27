# Applications (Its a FIFO Data Structure):
# Queue of any kind | Background Tasks | Uploading Resources | Printing / Task Processing
# Big O of Queues - Insertion - O(1) | Removal - O(1) | Searching - O(N) | Access - O(N)

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def enqueue(self, val):
		newNode = Node(val)
		if self.first == None:
			self.first = newNode
			self.last = newNode
		else:
			self.last.next = newNode
			self.last = newNode
		self.size += 1
		return self

	def dequeue(self):
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

queue = Queue()
queue.enqueue(1).enqueue(2).enqueue(3).enqueue(4)
queue.traverse()
print(queue.dequeue())