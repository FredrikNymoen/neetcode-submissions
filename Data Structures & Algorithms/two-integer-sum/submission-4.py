class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            missing = target - num
            if missing in prevMap:
                return [prevMap[missing],i]
            prevMap[num] = i