class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1,len(nums) - 1
            missing = - num
            while l < r:
                sum = nums[l] + nums[r]
                if sum < missing:
                    l += 1
                elif sum > missing:
                    r -= 1
                else:
                    res.append([num,nums[l],nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        
        return res