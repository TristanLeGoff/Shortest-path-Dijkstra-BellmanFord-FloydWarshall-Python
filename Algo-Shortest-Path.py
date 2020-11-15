import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.graphEdge = []

    def set0toInf(self):
        INF = 99999  
        for i in range(self.V):  
            for j in range(self.V):
                if self.graph[i][j] == 0 and i != j:
                    self.graph[i][j] = INF

    def setInfto0(self):
        INF = 99999  
        for i in range(self.V):  
            for j in range(self.V):
                if self.graph[i][j] > 90000 :
                    self.graph[i][j] = 0

    def addEdges(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    self.graphEdge.append([i, j, self.graph[i][j]])

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print("From source to ",node, " it takes ", dist[node])


    def minDistance(self, dist, sptSet):

        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        self.setInfto0()
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

    def BellmanFord(self, src):
        self.setInfto0()

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graphEdge:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graphEdge:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("graphEdge contains negative weight cycle")
                return

        self.printSolution(dist)

    def FloydWarshall(self,src):
        self.set0toInf()
        copyG = self.graph
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if copyG[i][j] > copyG[i][k] + copyG[k][j]:
                        copyG[i][j] = copyG[i][k] + copyG[k][j]
        print("Complete matrix : \n",copyG)
        dist = copyG[src]
        self.printSolution(dist)

g = Graph(7)
g.graph = [[0, 3, 4, 0, 0, 0, 0],
           [0, 0, 1, 0, 3, 2, 0],
           [0, 0, 0, 3, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 2, 0, 3],
           [0, 0, 0, 0, 0, 0, 0]]
g.addEdges()

# g.dijkstra(0);

#g.BellmanFord(0)

g.FloydWarshall(0)

