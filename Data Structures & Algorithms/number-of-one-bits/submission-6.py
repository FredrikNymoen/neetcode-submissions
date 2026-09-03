class Solution:
    # OPTIMAL
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n:
            n &= n - 1 # n = n & (n - 1)
            res += 1
        
        return res