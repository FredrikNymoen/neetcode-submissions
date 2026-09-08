class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}  # { 3: 0, 4: 1, 5: 2 ....} # {key: value}

        for i,num in enumerate(nums):
            missing = target - num

            if missing in visited:
                return [visited[missing], i]
            
            visited[num] = i  
        