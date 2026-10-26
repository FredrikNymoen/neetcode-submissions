class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            missing = target - nums[i]

            if missing in seen:
                return [seen[missing],i]
            else:
                seen[nums[i]] = i
            
            