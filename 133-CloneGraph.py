"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optiaonal


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        trackHashmap = {}

        if not node:
            return None

        def dfs(node):
            if node in trackHashmap:
                return trackHashmap[node]

            copy = Node(node.val)
            trackHashmap[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
