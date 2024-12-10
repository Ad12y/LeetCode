class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        print(adj_list)
        start = -1
        cycle = set()
        visited = [False] * (n + 1)
        def dfs(node,par):
            nonlocal start 
            if visited[node]:
                start = node
                return True
            visited[node] = True
            for neigh in adj_list[node]:
                if neigh == par:
                    continue
                if dfs(neigh, node):
                    if start != -1:
                        cycle.add(node)
                    if node == start:
                        return
                    return True
        dfs(1, -1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []


        