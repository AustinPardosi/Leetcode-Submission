from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        count = 0
        visited = set()
        adj = defaultdict(list) # node: neighhbors

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node): # record everything into visited
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count