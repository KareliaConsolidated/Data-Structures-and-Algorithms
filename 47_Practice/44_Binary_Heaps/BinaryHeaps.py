class BinaryHeaps:
	def __init__(self):
		self.values = []

	def MaxHeapInsert(self, val):
		self.values.append(val)
		self.BubbleUp()

	def BubbleUp(self):
		idx = len(self.values) - 1 
		element = self.values[idx]
		while idx > 0:
			ParentIdx = (idx-1) // 2
			Parelement = self.values[ParentIdx]
			if element <= Parelement: break
			self.values[ParentIdx], self.values[idx] = self.values[idx], self.values[ParentIdx]
			idx = ParentIdx

	def MaxHeapRemove(self):
		maxHeap = self.values[0]
		end = self.values.pop()
		if len(self.values) > 0:
			self.values[0] = end
			self.BubbleDown()
		return maxHeap

	def BubbleDown(self):
		idx = 0
		length = len(self.values)
		element = self.values[0]

		while True:
			leftChildIdx = (2*idx) + 1
			rightChildIdx = (2*idx) + 2
			swap, leftChild, rightChild = None, None, None

			if leftChildIdx < length:
				leftChild = self.values[leftChildIdx]
				if leftChild > element:
					swap = leftChildIdx

			if rightChildIdx < length:
				rightChild = self.values[rightChildIdx]
				if ((swap == None and rightChild > element) or (swap != None and rightChild > leftChild)):
					swap = rightChildIdx

			if swap == None: break

			self.values[idx] = self.values[swap]
			self.values[swap] = element
			idx = swap

MaxHeap = BinaryHeaps()
MaxHeap.MaxHeapInsert(1)
MaxHeap.MaxHeapInsert(10)
MaxHeap.MaxHeapInsert(190)
MaxHeap.MaxHeapInsert(15)
MaxHeap.MaxHeapInsert(110)
MaxHeap.MaxHeapInsert(810)
print(MaxHeap.values)
print(MaxHeap.MaxHeapRemove())
print(MaxHeap.values)