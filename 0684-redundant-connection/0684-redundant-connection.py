class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #Trying union find to solve this problem
        rank = [1] *(len(edges)+1)
        par = [i for i in range(0, len(edges)+1)]
        print(rank, par)

        def find(node):
            p = par[node] 
            while p!=par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p 

        def union(a,b):
            a, b = find(a), find(b)
            if a == b:
                return False
            if rank[a] > rank[b]:
                par[b] = par[a]
                rank[a] += rank[b]
            else:
                par[a] = par[b]
                rank[b] += rank[a]
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v] 

