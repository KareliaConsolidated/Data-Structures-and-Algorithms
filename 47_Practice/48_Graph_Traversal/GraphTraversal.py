# ---------------------- PROBLEM 48 (RANDOM) ----------------------------------#
# A Graph is a non-linear data structure consisting of nodes and edges. 
# The nodes are sometimes also referred to as vertices and the edges are lines or 
# arcs that connect any two nodes in the graph.
# USES: Social Networks, Location/ Mapping, Routing Algos, Visual Hierarchy, File System Oraganizations.
class Graph:
	def __init__(self):
		self.adjacencyList = {}

# ----------------METHOD 01---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(|V| + |E|)
	def addVertex(self, vertex_name):
		if vertex_name not in self.adjacencyList:
			self.adjacencyList[vertex_name] = []
		return self.adjacencyList
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(|V| + |E|)
	def addEdge(self, vertex1, vertex2):
		self.adjacencyList[vertex1].append(vertex2)
		self.adjacencyList[vertex2].append(vertex1)
		return self.adjacencyList
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
	# COMPLEXITY = TIME: O(E), SPACE: O(1)
	def removeEdge(self, vertex1, vertex2):
		self.adjacencyList[vertex1].remove(vertex2)
		self.adjacencyList[vertex2].remove(vertex1)
		return self.adjacencyList
# ----------------METHOD 03---------------------#

# ----------------METHOD 04---------------------#
	# COMPLEXITY = TIME: O(|V| + |E|), SPACE: O(1)
	def removeVertex(self, vertex2):
		lst = self.adjacencyList[vertex2].copy()
		for vertex1 in lst:
			self.removeEdge(vertex1, vertex2)
		del self.adjacencyList[vertex2]
		return self.adjacencyList
# ----------------METHOD 04---------------------#

# ----------------METHOD 05---------------------#

	def DFSRecursive(self, vertex, results = []):
		lst = self.adjacencyList
		if lst[vertex] is None: return None
		results.append(vertex)
		for vert in self.adjacencyList[vertex]:
			if vert not in results:
				self.DFSRecursive(vert, results)
		return results

# ----------------METHOD 05---------------------#

# ----------------METHOD 06---------------------#

	def DFSIterative(self, vertex):
		lst = self.adjacencyList
		if lst[vertex] is None: return None
		stacks = []
		results = []
		stacks.append(vertex)
		while len(stacks) != 0:
			node = stacks.pop()
			results.append(node)
			for vert in lst[node]:
				if vert not in results and vert not in stacks:
					stacks.append(vert)
		return results

# ----------------METHOD 06---------------------#

# ----------------METHOD 07---------------------#

	def BFSIterative(self, vertex):
		lst = self.adjacencyList
		if lst[vertex] is None: return None

		results = []
		queue = [vertex]
		while len(queue) != 0:
			node = queue.pop(0)
			results.append(node)
			for vert in lst[node]:
				if vert not in queue and vert not in results:
					queue.append(vert)
		return results					

# ----------------METHOD 07---------------------#

# ----------------Weighted Graph---------------------#
class WeightedGraph:
	def __init__(self):
		self.adjacencyList = {}

# ----------------METHOD 01---------------------#
	
	def addVertex(self, vertex_name):
		if vertex_name not in self.adjacencyList:
			self.adjacencyList[vertex_name] = []
		return self.adjacencyList

# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
	
	def addEdge(self, vertex1, vertex2, weight):
		self.adjacencyList[vertex1].append({"node":vertex2, "weight": weight})
		self.adjacencyList[vertex2].append({"node":vertex1, "weight": weight})
		return self.adjacencyList

# ----------------METHOD 02---------------------#
print('****************************')


graph_rec = Graph()
graph_rec.addVertex('A')
graph_rec.addVertex('B')
graph_rec.addVertex('C')
graph_rec.addVertex('D')
graph_rec.addVertex('E')
graph_rec.addVertex('F')
graph_rec.addEdge('A', 'B')
graph_rec.addEdge('A', 'C')
graph_rec.addEdge('B', 'D')
graph_rec.addEdge('C', 'E')
graph_rec.addEdge('D', 'E')
graph_rec.addEdge('D', 'F')
print(graph_rec.addEdge('F', 'E'))
print(graph_rec.DFSRecursive('A'))  # ['A', 'B', 'D', 'E', 'C', 'F']
print(graph_rec.DFSIterative('A'))  # ['A', 'C', 'E', 'F', 'D', 'B']
print(graph_rec.BFSIterative('B'))  # ['B', 'A', 'D', 'C', 'E', 'F']

weightedGraph = WeightedGraph()
weightedGraph.addVertex("A")
weightedGraph.addVertex("B")
weightedGraph.addVertex("C")
print(weightedGraph.addEdge("A", "B", 250)) # {'A': [{'node': 'B', 'weight': 250}], 'B': [{'node': 'A', 'weight': 250}], 'C': []}
print(weightedGraph.addEdge("C", "B", 30)) # {'A': [{'node': 'B', 'weight': 250}], 'B': [{'node': 'A', 'weight': 250}, {'node': 'C', 'weight': 30}], 'C': [{'node': 'B', 'weight': 30}]}