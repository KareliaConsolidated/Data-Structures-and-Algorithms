class WeightedGraph:
	def __init__(self):
		self.adjacencyList = {}

	def addVertex(self, vertex):
		if vertex not in self.adjacencyList:
			self.adjacencyList[vertex] = []
		return self.adjacencyList

	def addEdge(self, vert01, vert02, weight):
		self.adjacencyList[vert01].append({"node":vert02, "weight":weight})
		self.adjacencyList[vert02].append({"node":vert01, "weight":weight})
		return self.adjacencyList

	def Dijkstra(self, start, finish):
		queue = PriorityQueue()
		distance = {}
		previous = {}
		smallest = None
		path = []

		for vertex in self.adjacencyList:
			if vertex == start:
				distance[vertex] = 0
				queue.enqueue(vertex, 0)
			else:
				distance[vertex] = float('inf')
				queue.enqueue(vertex, float('inf'))
			previous[vertex] = None

		while len(queue.values) != 0:
			smallest = queue.dequeue()['val']
			
			if smallest == finish:
				while smallest != None:
					path.append(smallest)
					smallest = previous[smallest]
				break

			for neigh in self.adjacencyList[smallest]:
				candidate_dist = distance[smallest] + neigh['weight']
				if candidate_dist < distance[neigh['node']]:
					distance[neigh['node']] = candidate_dist
					previous[neigh['node']] = smallest
					queue.enqueue(neigh['node'], candidate_dist)

		return path[::-1]

class PriorityQueue:
	def __init__(self):
		self.values = []

	def enqueue(self, val, priority):
		self.values.append({"val":val, "priority":priority})
		self.sort()
		return self.values
	
	def dequeue(self):
		return self.values.pop(0)

	def sort(self):
		self.values = sorted(self.values, key=lambda x: x['priority'])

weightedGraph = WeightedGraph()
weightedGraph.addVertex("A")
weightedGraph.addVertex("B")
weightedGraph.addVertex("C")
weightedGraph.addVertex("D")
weightedGraph.addVertex("E")
weightedGraph.addVertex("F")
weightedGraph.addEdge("A", "B", 4)
weightedGraph.addEdge("A", "C", 2)
weightedGraph.addEdge("C", "D", 2)
weightedGraph.addEdge("C", "F", 4)
weightedGraph.addEdge("D", "E", 3)
weightedGraph.addEdge("D", "F", 1)
weightedGraph.addEdge("E", "F", 1)
weightedGraph.addEdge("E", "B", 3)
print(weightedGraph.Dijkstra("A", "E"))