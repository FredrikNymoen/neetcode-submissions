class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        prev2, prev1 = 0, 0

        for n in nums:
            tmp = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = tmp
        
        return prev1