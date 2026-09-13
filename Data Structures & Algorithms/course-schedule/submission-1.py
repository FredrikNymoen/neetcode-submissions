class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visited:
                return False
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            preMap[crs] = []
            visited.remove(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True