class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        nums.sort()
        cur = nums[0]

        for i in range(1,len(nums)):
            if cur == nums[i]:
                return True
            
            cur = nums[i]
        return False