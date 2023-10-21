"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np


class AdjacencyMatrix():
    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=bool)

    def add_edge(self, i: int, j: int):
        if 0 <= i and j < self.n:
            self.adj[i][j] = True

    def remove_edge(self, i: int, j: int):
        if self.adj[i][j]:
            self.adj[i][j] = False
            return True
        return False

    def has_edge(self, i: int, j: int) -> bool:
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        edges = []
        for j in range(len(self.adj[i])):
            if self.adj[i][j]:
                edges.append(j)
        return edges

    def in_edges(self, j) -> List:
        edges = []
        for i in range(len(self.adj)):
            if self.adj[i][j]:
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
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def size(self):
        return self.n
