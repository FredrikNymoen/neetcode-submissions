class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()     # O(n)

        for num in nums: # O(n)
            if num in visited:
                return True
            visited.add(num)
        
        return False