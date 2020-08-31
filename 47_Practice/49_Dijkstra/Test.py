class WeightedGraph:
	def __init__(self):
		self.adjacencyList = {}

	def addVertex(self, vertex):
		if vertex not in self.adjacencyList:
			self.adjacencyList[vertex] = []
		return self.adjacencyList

	def addEdge(self, vert01, vert02, weight):
		self.adjacencyList[vert01] = {'node': vert02, 'weight': weight}
		self.adjacencyList[vert02] = {'node': vert01, 'weight': weight}
		return self.adjacencyList