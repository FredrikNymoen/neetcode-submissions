class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(i,prev):
            if i in visited:
                return False
            
            visited.add(i)
            
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei,i):
                    return False
            
            return True
        
        return dfs(0,-1) and n == len(visited)