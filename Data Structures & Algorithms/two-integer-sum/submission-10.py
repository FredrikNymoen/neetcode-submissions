class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for y in range(len(nums)):
                if nums[n]+nums[y]==target and n!=y:
                    return [n, y]

            