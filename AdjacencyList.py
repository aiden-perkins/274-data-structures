"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np

 
class AdjacencyList(Graph):
    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i: int, j: int):
        if not self.adj[i].contains(j):
            self.adj[i].append(j)

    def remove_edge(self, i: int, j: int):
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i: int, j: int) -> bool:
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                return True
        return False
        
    def out_edges(self, i) -> List:
        return self.adj[i]
 
    def in_edges(self, j) -> List:
        edges = []
        for i in range(len(self.adj)):
            if self.has_edge(i, j):
                edges.append(i)
        return edges
    
    def bfs(self, r: int):
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n, dtype=bool)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while q.size() > 0:
            for neighbor in self.out_edges(q.remove()):
                if not seen[neighbor]:
                    q.add(neighbor)
                    traversal.append(neighbor)
                    seen[neighbor] = True
        return traversal
 
    def dfs(self, r: int):
        traversal = ArrayList.ArrayList()
        s = ArrayStack.ArrayStack()
        seen = np.zeros(self.n, dtype=bool)
        s.push(r)
        while s.size() > 0:
            current = s.pop()
            if not seen[current]:
                traversal.append(current)
                seen[current] = True
            for neighbor in reversed(self.out_edges(current)):
                if not seen[neighbor]:
                    s.push(neighbor)
        return traversal
          
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
    
    def size(self):
        return self.n
