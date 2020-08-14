class Graphs:
	def __init__(self):
		self.adjacencyList = {}

	def addVertex(self, vert):
		if vert not in self.adjacencyList:
			self.adjacencyList[vert] = []
		return self.adjacencyList

	def addEdge(self, vert_01, vert_02):
		self.adjacencyList[vert_01].append(vert_02)
		self.adjacencyList[vert_02].append(vert_01)
		return self.adjacencyList

	def removeEdge(self, vert_01, vert_02):
		self.adjacencyList[vert_01].remove(vert_02)
		self.adjacencyList[vert_02].remove(vert_01)
		return self.adjacencyList

	def removeVertex(self, vert):
		lst = self.adjacencyList[vert].copy()
		for i in lst:
			self.removeEdge(vert, i)
		del self.adjacencyList[vert]
		return self.adjacencyList

graph = Graphs()
graph.addVertex('Tokyo')
graph.addVertex('Dallas')
graph.addVertex('Aspen')
graph.addVertex('Hong Kong')
graph.addVertex('Los Angeles')
graph.addEdge('Hong Kong','Tokyo')
graph.addEdge('Aspen','Dallas')
graph.addEdge('Los Angeles','Dallas')
graph.addEdge('Hong Kong','Dallas')
graph.addEdge('Dallas','Tokyo')
print(graph.addEdge('Los Angeles','Hong Kong'))
# {'Tokyo': ['Hong Kong', 'Dallas'], 
# 'Dallas': ['Aspen', 'Los Angeles', 'Hong Kong', 'Tokyo'], 
# 'Aspen': ['Dallas'], 
# 'Hong Kong': ['Tokyo', 'Dallas', 'Los Angeles'], 
# 'Los Angeles': ['Dallas', 'Hong Kong']}

# print(graph.removeEdge('Hong Kong','Dallas'))
print(graph.removeVertex("Hong Kong"))
# {'Tokyo': ['Dallas'], 
# 'Dallas': ['Aspen', 'Los Angeles', 'Tokyo'], 
# 'Aspen': ['Dallas'], 'Los Angeles': ['Dallas']}
