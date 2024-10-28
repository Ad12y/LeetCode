"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(ptr):
            if ptr in visited:
                return visited[ptr]
            clone = Node(ptr.val)
            visited[ptr] = clone
            for i in ptr.neighbors:
                clone.neighbors.append(dfs(i))
            return clone

        ptr = node
        if not ptr:
            return ptr

        return dfs(ptr)




        