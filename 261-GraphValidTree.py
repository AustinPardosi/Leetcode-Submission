from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # VAlID TREE
        # - No Cyclic
        # - All node needs to be connected

        # Rule 1: A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n-1:
            return False

        visited = set()
        adj = defaultdict(list) # node : [neighbors]

        # Build adj
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node, prevNode): # DFS to check is the graph has cycle or not
            # set visited
            visited.add(node)

            # Travel to all the neighbor
            for neighbor in adj[node]:
                if neighbor == prevNode: # Skip the edge we just come
                    continue
                if neighbor in visited:
                    return True # Cyclic
                if dfs(neighbor, node):
                    return True
            return False # We traverse all the neighbor but no cyclic
        
        # Rule 2: Run DFS starting from node 0.
        if dfs(0, -1):
            return False
        
        # Rule 3: Check if all nodes were visited (ensures no disconnected pieces)
        return len(visited) == n