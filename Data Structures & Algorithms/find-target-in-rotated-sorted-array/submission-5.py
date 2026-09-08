class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        idx = -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                idx = m
                break

            # sorted left side
            elif nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # sorted right side
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return idx

        #          l   r
        # [4,5,6,7,0,1,2]
        # nums[m] = 1