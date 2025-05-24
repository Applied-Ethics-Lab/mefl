# datastructures/graphs.py

import heapq

class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}  # node: list of (neighbor, weight)
        self.directed = directed

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))

    def neighbors(self, node):
        return self.adj_list.get(node, [])

    def bfs(self, start, visit_func):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            visit_func(node)
            for neighbor, _ in self.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start, visit_func, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        visit_func(start)
        for neighbor, _ in self.neighbors(start):
            if neighbor not in visited:
                self.dfs(neighbor, visit_func, visited)

    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.adj_list}
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)
            if current_dist > dist[current_node]:
                continue
            for neighbor, weight in self.neighbors(current_node):
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        return dist

# Example usage:
if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 1)
    g.add_edge("B", "C", 7)
    g.add_edge("C", "D", 2)

    print("BFS from A:")
    g.bfs("A", print)

    print("DFS from A:")
    g.dfs("A", print)

    print("Dijkstra from A:")
    print(g.dijkstra("A"))
